from django.contrib import admin
from .models import Post, Comment, Mention, Reaction, Notification, Story
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Mention)
admin.site.register(Reaction)
admin.site.register(Notification)
admin.site.register(Story)