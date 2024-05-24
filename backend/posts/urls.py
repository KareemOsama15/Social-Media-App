from django.urls import path
from .views import (PostCreateApiView,
                    PostListRetrieveApiView,
                    PostDestroyApiView,
                    PostUpdateApiView,
                    LikePostApiView,
                    CommentCreateApiView,
                    CommentListRetrieveApiView,
                    CommentDestroyApiView,
                    CommentUpdateApiView
                    )

urlpatterns = [
    path('', PostListRetrieveApiView.as_view()),
    path('<int:pk>/', PostListRetrieveApiView.as_view()),
    path('create/',  PostCreateApiView.as_view()),
    path('<int:pk>/update/', PostUpdateApiView.as_view()),
    path('<int:pk>/delete/', PostDestroyApiView.as_view()),
    path('<int:pk>/like/', LikePostApiView.as_view()),
    path('<int:pk>/comment/', CommentListRetrieveApiView.as_view()),
    path('<int:pk>/comment/create/',  CommentCreateApiView.as_view()),
    path('<int:post_id>/comment/<int:pk>/update/', CommentUpdateApiView.as_view()),
    path('<int:post_id>/comment/<int:pk>/delete/', CommentDestroyApiView.as_view()),
]
