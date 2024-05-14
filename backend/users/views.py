# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class SignUpView(GenericAPIView):
    """
    SignUpView class handle sign-up process
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = serializer.data
            data['tokens'] = {'refresh': str(token), 'access': str(token.access_token)}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    """
    LoginView class that handles login process
    """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token = RefreshToken.for_user(user)
            data = {
                'message': 'Login successful',
                'tokens': {'refresh': str(token), 'access': str(token.access_token)}
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(GenericAPIView):
    """
    LogoutView class that handles logout process
    """
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status= status.HTTP_400_BAD_REQUEST)
