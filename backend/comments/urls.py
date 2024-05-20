from django.urls import path
from .views import CommentCreate, CommentOfPost, CommentDelete

urlpatterns = [
    path('<int:pk>/', CommentOfPost.as_view()),
    path('create/',  CommentCreate.as_view()),
    path('<int:pk>/delete/', CommentDelete.as_view()),
]
