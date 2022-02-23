from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    ip_address = serializers.CharField(max_length=14)
    text = serializers.CharField()
    token = serializers.CharField(max_length=19)
