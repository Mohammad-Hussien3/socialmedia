from django.db import models
from usermanagement.models import Profile
# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', blank=True)

    def __str__(self):
        return f'{self.content} {self.id}'
    
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.content} {self.id}'