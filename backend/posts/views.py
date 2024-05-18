from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer, ListRetrievePostSerializer
from django.shortcuts import get_object_or_404

class PostCreateApiView(generics.CreateAPIView):
    """from django.shortcuts import get_object_or_404
    class view implements creating a new post instance
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostListRetrieveApiView(generics.ListAPIView, generics.RetrieveAPIView):
    """
    class view lists all objects of Post class in database
    , and retrieves a single post item
    """
    queryset = Post.objects.all()
    serializer_class = ListRetrievePostSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'
    # parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

class PostUpdateApiView(generics.UpdateAPIView):
    """Class view updates a Post instance """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        user = str(request.user)
        if user == post.author.email:
            return self.update(request, *args, **kwargs)
        return Response({'message': 'Update Post Not Allowed'}, status=status.HTTP_400_BAD_REQUEST)


class PostDestroyApiView(generics.DestroyAPIView):
    """Class view destroys a Post instance """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        user = str(request.user)
        if user == post.author.email:
            return self.destroy(request, *args, **kwargs)
        return Response({'message': 'Delete Post Not Allowed'}, status=status.HTTP_400_BAD_REQUEST)
