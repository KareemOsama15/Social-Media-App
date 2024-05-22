from django.urls import path
from .views import (PostCreateApiView,
                    PostListRetrieveApiView,
                    PostDestroyApiView,
                    PostUpdateApiView,
                    LikePostApiView,
                    )

urlpatterns = [
    path('', PostListRetrieveApiView.as_view()),
    path('<int:pk>/', PostListRetrieveApiView.as_view()),
    path('create/',  PostCreateApiView.as_view()),
    path('<int:pk>/update/', PostUpdateApiView.as_view()),
    path('<int:pk>/delete/', PostDestroyApiView.as_view()),
    path('<int:pk>/like/', LikePostApiView.as_view()),
]
