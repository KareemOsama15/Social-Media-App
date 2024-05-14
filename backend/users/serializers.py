from rest_framework import serializers
from .models import CustomUser

class UserSignUpSerializer(serializers.ModelSerializer):
    """
    UserSignUpSerializer class serialize CustomUser data fields
    and validates it for sign-up process
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """method creates and returns a new instance of user"""
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        """method validates the user sended password"""
        password = attrs.get("password", "")
        if len(password) < 8:
            raise serializers.ValidationError(
                "Passwords must be at least 8 characters!")
        return attrs

class UserLoginSerializer(serializers.ModelSerializer):
    """
    UserLoginSerializer class serialize CustomUser data fields
    and validates it for login process
    """
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
