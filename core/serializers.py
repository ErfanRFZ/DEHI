from custom_validation_error import CustomSerializer


class ExampleSerializer(CustomSerializer):

    def validate_serializer(self, attrs, error_obj):
        return attrs
