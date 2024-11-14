from rest_framework import generics
from rest_framework.views import Response, status, APIView
from .models import Post
from .serializers import PostSerializer, CommentSerializer, MentionSerilizer, ReactionSerializer
from rest_framework.permissions import IsAuthenticated

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