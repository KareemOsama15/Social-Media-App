from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .serializers import CreatePostSerializer, ListPostSerializer

class PostCreateApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        image = request.data.get('image')
        print(f'image = {image}')
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser, FormParser]
