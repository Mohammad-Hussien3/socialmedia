from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import Response, status
from django.contrib.auth import authenticate
# Create your views here.

def check_keys(expected_keys, received_keys):
    return received_keys == expected_keys


def error_keys(expected_keys, received_keys):
    return Response(
                {'error': 'Invalid keys in the request data.', 'expected': list(expected_keys), 'received': list(received_keys)},
                status=status.HTTP_400_BAD_REQUEST
            )


class TokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LogOut(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class LogIn(APIView):

    expected_keys = {'username', 'password'}
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        received_keys = set(data.keys())
        if not check_keys(self.expected_keys, received_keys):
            return error_keys(self.expected_keys, received_keys)
        
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token = RefreshToken.for_user(user)
            return Response({'token': str(token.access_token), 'refresh': str(token)}, status=status.HTTP_200_OK)
        
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class FollowUser(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, userId, userToFollowId):
        userProfile = get_object_or_404(Profile, user__id=userId)
        userToFollow = get_object_or_404(Profile, user__id=userToFollowId)
        userToFollow.followers.add(userProfile)
        userToFollow.save()
        return Response({'message':'success'})
    

class UnfollowUser(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, userId, userNotToFollowId):
        userProfile = get_object_or_404(Profile, user__id=userId)
        userToFollow = get_object_or_404(Profile, user__id=userNotToFollowId)
        userToFollow.followers.remove(userProfile)
        userToFollow.save()
        return Response({'message':'success'})