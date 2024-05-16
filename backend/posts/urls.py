from django.urls import path
from .views import PostCreateApiView, PostListRetrieveApiView

urlpatterns = [
    path('', PostListRetrieveApiView.as_view()),
    path('<int:pk>/', PostListRetrieveApiView.as_view()),
    path('create/',  PostCreateApiView.as_view()),
]
