from rest_framework import serializers
from .models import Comment
from users.models import CustomUser

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username',read_only=True) # it this the right way or shoulr i use 'CustomUser'?

	class Meta:
		model = Comment
		fields = '__all__'
