from rest_framework import serializers
from .models import Post, Comment

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
    likes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id',
                  'username',
                  'content',
                  'image',
                  'created_at',
                  'updated_at',
                  'likes',
                  'comments',
                  ]

    def get_username(self, obj):
        """serializer method to get instance username"""
        return obj.author.username

    def get_likes(self, obj):
        return obj.num_of_likes

    def get_comments(self, obj):
        return obj.all_comments


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = ['content']
