from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import CreatePostSerializer, ListRetrievePostSerializer

class PostCreateApiView(generics.CreateAPIView):
    """
    class view implements creating a new post instance
    """
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
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
