from django.db import models
from posts.models import Post
from users.models import CustomUser

class Comment(models.Model):
    """class for Comment of the Post model"""
    content = models.TextField(null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # likes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.author.username} - {self.content[:25]}...Read More"

    class Meta:
        ordering = ['-updated_at', '-created_at']
