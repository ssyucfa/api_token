from django.core.validators import RegexValidator
from rest_framework import serializers

from tokens.models import Token


class TokenSerializer(serializers.Serializer):
    ip_address = serializers.CharField(max_length=14, validators=[RegexValidator(
        regex=r'^\d{3}.\d{3}.\d{2}.\d{3}$',
        message='Ip address must like XXX.XXX.XX.XXX',
        code='invalid ip address'
    )])
    text = serializers.CharField()
    token = serializers.CharField(max_length=19, validators=[RegexValidator(
        regex=r'^\d{4}-\d{4}-\d{4}-\d{4}$',
        message='Token must like XXXX-XXXX-XXXX-XXXX',
        code='invalid token'
    )])

    def save(self, **kwargs) -> None:
        data_token = self.validated_data['token']

        token = Token.objects.get(token=data_token)
        token.is_using = True

        token.save()
