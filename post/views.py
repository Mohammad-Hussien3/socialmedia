from rest_framework import generics
from rest_framework.views import Response, status, APIView
from .models import Notification
from .serializers import PostSerializer, CommentSerializer, MentionSerilizer, ReactionSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# Create your views here.

def check_keys(expected_keys, received_keys):
    return received_keys == expected_keys


def error_keys(expected_keys, received_keys):
    return Response(
                {'error': 'Invalid keys in the request data.', 'expected': list(expected_keys), 'received': list(received_keys)},
                status=status.HTTP_400_BAD_REQUEST
            )


class AddPost(generics.CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer


class AddComment(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer


class CreateMention(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = MentionSerilizer


class AddReaction(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ReactionSerializer


class MarkNotificationAsRead(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        notification = get_object_or_404(Notification, id=id)
        notification.isRead = True
        notification.save()
        return Response({'message':'success'}, status=status.HTTP_200_OK)
    

class GetMyNotifications(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer