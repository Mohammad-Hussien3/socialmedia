from django.db import models
# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contect} {self.id}'