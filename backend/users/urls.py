from django.urls import path
from .views import SignUpView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]
