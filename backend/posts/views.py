from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Post, Like, Comment
from .serializers import PostSerializer, ListRetrievePostSerializer, CommentSerializer
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

class LikePostApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id)
        like_exist = Like.objects.filter(author=request.user, post=post).first()
        if like_exist:
            like_exist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        Like.objects.create(author=request.user, post=post)
        return Response(status=status.HTTP_201_CREATED)


class CommentCreateApiView(generics.CreateAPIView):
    """from django.shortcuts import get_object_or_404
    class view implements creating a new comment instance
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        serializer = self.get_serializer(data=request.data)
        
        post = get_object_or_404(Post, pk=pk)
        
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer, post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer, post):
        serializer.save(author=self.request.user, post=post)

class CommentListRetrieveApiView(generics.ListAPIView, generics.RetrieveAPIView):
    """
    class view lists all objects of comment class in database
    , and retrieves a single post item
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'pk'
    # parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        comment_pk = kwargs.get('pk')
        if comment_pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

class CommentUpdateApiView(generics.UpdateAPIView):
    """Class view updates a comment instance """
    """queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = ['post_id', 'pk']

    def put(self, request, *args, **kwargs):
        post_pk = kwargs.get('post_id')
        comment_pk = kwargs.get('pk')
        comment = get_object_or_404(Comment, pk=comment_pk)
        post = get_object_or_404(Post, pk=post_pk)
        user = str(request.user)
        if user == comment.author.email:
            return self.update(request, *args, **kwargs)
        return Response({'message': 'Update Comment Not Allowed'}, status=status.HTTP_400_BAD_REQUEST)
"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = ['post_id', 'pk']

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter_kwargs = {
            'id': self.kwargs['pk'],
            'post_id': self.kwargs['post_id']
        }
        obj = generics.get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied("Permisssion denied")
        serializer.save()





    """def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
"""


class CommentDestroyApiView(generics.DestroyAPIView):
    """Class view destroys a comment instance """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = ['post_id', 'pk']

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter_kwargs = {
            'id': self.kwargs['pk'],
            'post_id': self.kwargs['post_id']
        }
        obj = generics.get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_destroy(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied("Permisssion denied")
        serializer.save()

"""    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

   def delete(self, request, *args, **kwargs):
        comment_pk = kwargs.get('pk')
        comment = get_object_or_404(Comment, pk=pk)
        user = str(request.user)
        if user == comment.author.email:
            return self.destroy(request, *args, **kwargs)
        return Response({'message': 'Delete Comment Not Allowed'}, status=status.HTTP_400_BAD_REQUEST)
"""
