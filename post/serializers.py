from rest_framework import serializers
from .models import Post, Comment, Mention, Reaction

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'image', 'uploadedAt', 'profile']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'uploadedAt', 'post']


class MentionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'profile', 'post']


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'profile', 'post', 'reactionType', 'createdAt']