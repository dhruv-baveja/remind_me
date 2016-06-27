from django.contrib.auth.models import User

from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=5)
    confirm_password = serializers.CharField(min_length=5)

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value):
            raise serializers.ValidationError("User corresponding to email already exist")
        return value

    @staticmethod
    def validate(data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password and Current Password mismatch")
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=5)
