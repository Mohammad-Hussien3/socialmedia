from django.db import models
from usermanagement.models import Profile
# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    uploadedAt = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', blank=True)

    def __str__(self):
        return f'{self.content} {self.id}'
    
    class Meta:
        ordering = ['-uploadedAt']
    
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    uploadedAt = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return f'{self.content} {self.id}'
    
    class Meta:
        ordering = ['-uploadedAt']
    

class Mention(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mention')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='mention')

    def __str__(self):
        return f'{self.profile.user.username} postId:{self.post.id} mentionId:{self.id}'
    

class Reaction(models.Model):
    LIKE = 'like'
    LOVE = 'love'
    HAHA = 'haha'
    SAD = 'sad'
    ANGRY = 'angry'
    
    REACTION_TYPES = [
        (LIKE, 'Like'),
        (LOVE, 'Love'),
        (HAHA, 'Haha'),
        (SAD, 'Sad'),
        (ANGRY, 'Angry'),
    ]

    reactionType = models.CharField(max_length=5, choices=REACTION_TYPES, default=LIKE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reactions')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile.user.username} postId:{self.post.id} reactionId:{self.id}'
    
    class Meta:
        ordering = ['-createdAt']
    

class Notification(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='sent_notifications')
    receive = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_notifications')
    content = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification from {self.sender} to {self.receive}'
    
    class Meta:
        ordering = ['-createdAt']


class Story(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stories')
    content = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content} time: {self.createdAt}'
    
    class Meta:
        ordering = ['-createdAt']