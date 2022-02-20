from typing import Union, Type

from django.utils import timezone
from rest_framework import views, status
from rest_framework.response import Response

from tokens.models import Token
from tokens.serializers import TokenSerializer
from tokens.service import request_to_third_party_api


class TokenView(views.APIView):
    serializer_class = TokenSerializer
    model = Token

    @staticmethod
    def _is_token_exist(token) -> Union[bool, Type[Token]]:
        try:
            token = Token.objects.get(token=token)
        except Token.DoesNotExist:
            return False
        return token

    @staticmethod
    def _set_a_field_is_using_to_false_and_time_to_now(token) -> None:
        token.last_join = timezone.now()
        token.is_using = False
        token.save()

    @staticmethod
    def _get_a_field_is_using_from_token_model(token) -> False:
        return token.is_using

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        token = self._is_token_exist(serializer.data.get('token'))
        if not token:
            return Response(
                {
                    'error': 'Token is not exist'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        elif self._get_a_field_is_using_from_token_model(token):
            return Response(
                {
                    'error': 'Token is already using'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        data_token, ip_address, text = request_to_third_party_api(
            serializer.data.get('token'),
            serializer.data.get('ip_address'),
            serializer.data.get('text')
        )

        self._set_a_field_is_using_to_false_and_time_to_now(token)

        return Response(
            {
                'token': data_token,
                'ip_address': ip_address,
                'text': text
            },
            status=status.HTTP_200_OK
        )
