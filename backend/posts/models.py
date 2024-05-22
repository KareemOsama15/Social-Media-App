from django.db import models
from users.models import CustomUser


class Post(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return f"{self.author.username} - {self.content[:25]}...Read More"

    @property
    def num_of_likes(self):
        """property to return a number of likes on post"""
        return Like.objects.filter(post=self.id).count()

"""class Connection(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = (('from_user', 'to_user'),)
"""

class Like(models.Model):
    """Model class for adding Like from user to a post"""
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
