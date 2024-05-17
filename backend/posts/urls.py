from django.urls import path
from .views import PostCreateApiView, PostListRetrieveApiView, PostDestroyApiView, PostUpdateApiView

urlpatterns = [
    path('', PostListRetrieveApiView.as_view()),
    path('<int:pk>/', PostListRetrieveApiView.as_view()),
    path('create/',  PostCreateApiView.as_view()),
    path('<int:pk>/update/', PostUpdateApiView.as_view()),
    path('<int:pk>/destroy/', PostDestroyApiView.as_view()),
]
