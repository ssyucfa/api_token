from typing import Union, Type

from rest_framework import views, status
from rest_framework.response import Response

from tokens.models import Token
from tokens.serializers import TokenSerializer
from tokens.service import magic


class TokenView(views.APIView):
    serializer_class = TokenSerializer
    model = Token

    @staticmethod
    def _is_token_exist(token) -> Union[bool, Token]:
        try:
            token = Token.objects.get(token=token)
        except Token.DoesNotExist:
            return False
        return token

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
        ip_address = serializer.data.get('ip_address')
        if not token.is_using(ip_address):
            token.set_last_join_and_ip_address(ip_address)
            message = magic(serializer.data.get('text'))
            return Response(
                {
                    'message': message
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'error': 'Token is already using by another ip'
            },
            status=status.HTTP_400_BAD_REQUEST
        )






