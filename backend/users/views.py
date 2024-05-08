# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class SignUpView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            data = serializer.data
            data['tokens'] = {'refresh': str(token), 'access': str(token.access_token)}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(GenericAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(email=email, password=password)
#         if user:
#             token = RefreshToken.for_user(user)
#             return Response({'refresh': str(token), 'access': str(token.access_token)})
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print('='*10)
        print(request)
        print(request.data)
        print(f'\nemail={email}\npassword={password}')
        user = authenticate(email=email, password=password)
        print(f'\nuser={user}')
        if user:
            print('User authenticated successfully\n')
            print('='*10)
            token = RefreshToken.for_user(user)
            data = {
                'message': 'Login successful',
                'tokens': {'refresh': str(token), 'access': str(token.access_token)}
            }
            return Response(data)
        print('User authenticated Failled\n')
        print('='*10)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(status= status.HTTP_400_BAD_REQUEST)
