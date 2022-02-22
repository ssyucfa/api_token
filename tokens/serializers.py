from django.core.validators import RegexValidator
from rest_framework import serializers

from tokens.models import Token


class TokenSerializer(serializers.Serializer):
    ip_address = serializers.CharField(max_length=14)
    text = serializers.CharField()
    token = serializers.CharField(max_length=19)

    def save(self, **kwargs) -> None:
        data_token = self.validated_data['token']

        token = Token.objects.get(token=data_token)
        token.is_using = True

        token.save()
