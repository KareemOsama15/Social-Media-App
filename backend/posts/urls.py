from django.urls import path
from .views import PostCreateApiView, PostListApiView

urlpatterns = [
    path('', PostListApiView.as_view()),
    path('create/',  PostCreateApiView.as_view()),
]
