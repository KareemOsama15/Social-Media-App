from django.db import models
from users.models import CustomUser


class Post(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.author.username} - {self.content[:25]}...Read More"

    class Meta:
        ordering = ['-updated_at', '-created_at']


"""class Connection(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = (('from_user', 'to_user'),)
"""