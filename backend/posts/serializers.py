from rest_framework import serializers
from .models import Post

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content', 'image']

class ListPostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['username', 'content', 'image']

    def get_username(self, obj):
        return obj.author.username
