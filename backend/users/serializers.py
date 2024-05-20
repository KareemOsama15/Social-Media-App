from rest_framework import serializers
from .models import CustomUser

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        password = attrs.get("password", "")
        if len(password) < 8:
            raise serializers.ValidationError(
                "Passwords must be at least 8 characters!")

        return attrs

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
