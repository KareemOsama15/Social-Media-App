from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    serialize and validate data of creating a post
    """
    class Meta:
        model = Post
        fields = ['content', 'image']

class ListRetrievePostSerializer(serializers.ModelSerializer):
    """
    serialize post's data to implement list posts or retrieve a single one 
    """
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'content', 'image', 'created_at', 'updated_at']

    def get_username(self, obj):
        return obj.author.username
