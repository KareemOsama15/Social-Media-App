from django.urls import path
from .views import SignUpView, LoginView, LogoutView, UserInfoView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('users-info/', UserInfoView.as_view())
]
