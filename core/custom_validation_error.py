from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CustomSerializer(serializers.Serializer):
    def validate_serializer(self, attrs, error_obj):
        return attrs


class CustomModelSerializer(serializers.ModelSerializer, CustomSerializer):
    pass


class BaseCustomException(ValidationError):
    pass
