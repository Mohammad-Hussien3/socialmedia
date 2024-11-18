from rest_framework import generics
from rest_framework.views import Response, status, APIView
from .models import Notification, Post, Comment
from .serializers import PostSerializer, CommentSerializer, MentionSerilizer, ReactionSerializer, NotificationSerializer, StorySerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from usermanagement.models import Profile

# Create your views here.

def check_keys(expected_keys, received_keys):
    return received_keys == expected_keys


def error_keys(expected_keys, received_keys):
    return Response(
                {'error': 'Invalid keys in the request data.', 'expected': list(expected_keys), 'received': list(received_keys)},
                status=status.HTTP_400_BAD_REQUEST
            )


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


# Posts
class AddPost(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class GetMyPosts(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        profileId = self.kwargs.get('id')
        posts = Post.objects.filter(profile__id=profileId)
        return posts
    

class TrendingPosts(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        profile = Profile.objects.get(user__id=id)
        following = profile.following.all()
        posts = Post.objects.filter(profile__in=following)
        posts = sorted(posts, key=lambda x: len(x.reactions.all()), reverse=True)
        jsonPosts = PostSerializer(posts, many=True).data
        return Response(jsonPosts, status=status.HTTP_200_OK)


# Comments
class AddComment(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class GetMyComments(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        profileId = self.kwargs.get('id')
        comments = Comment.objects.filter(profile__id=profileId)
        return comments


class GetPostCommetns(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        postId = self.kwargs.get('postId')
        comments = Comment.objects.filter(post__id=postId)
        return comments
    

# Mentions
class CreateMention(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = MentionSerilizer


# Reactions
class AddReaction(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ReactionSerializer


# Notifications
class MarkNotificationAsRead(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        notification = get_object_or_404(Notification, id=id)
        notification.isRead = True
        notification.save()
        return Response({'message':'success'}, status=status.HTTP_200_OK)
    

class GetMyNotifications(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        profileId = self.kwargs.get('id')
        return Notification.objects.filter(receive__id=profileId)


class GetNotification(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'id'


# Stroy

class AddStory(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = StorySerializer