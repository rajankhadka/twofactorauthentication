from django.contrib.auth.models import User
from rest_framework import serializers
from authentication.models import PhoneNumber



class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, max_length=100)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data.get('username'),
            email=validate_data.get('email'),
        )
        user.set_password(validate_data.get('password'))
        user.save()
        return user
