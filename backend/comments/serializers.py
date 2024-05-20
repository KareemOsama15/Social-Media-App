from rest_framework import serializers
from .models import Comment
from users.models import CustomUser

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='self.request.user',read_only=True)

	class Meta:
		model = Comment
		fields = '__all__'
