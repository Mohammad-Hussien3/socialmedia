from django.urls import path
from . import views

urlpatterns = [
    # Token
    path('token/refresh/', views.TokenRefreshView.as_view(), name='refreshToken'),
    
    # Register
    path('signup/', views.SignUp.as_view(), name='signUp'),
    path('logout/<int:id>/', views.LogOut.as_view(), name='logOut'),
    path('login/', views.LogIn.as_view(), name='logIn'),

    # Following
    path('follow/<int:userId>/<int:userToFollowId>/', views.FollowUser.as_view(), name='followUser'),
    path('unfollow/<int:userId>/<int:userToUnfollowId>/', views.UnfollowUser.as_view(), name='unfollowUser'),
    path('getfollowers/<int:profileId>/', views.GetFollowers.as_view(), name='getFollowers'),
    path('getfollowing/<int:profileId>/', views.GetFollowing.as_view(), name='getFollowing'),

    # Pofile
    path('findprofile/<str:username>/', views.FindProfile.as_view(), name='findProfile'),
    path('homepage/<int:id>/', views.HomePage.as_view(), name='homePage'),
    path('getusers/', views.GetUsers.as_view(), name='getUsers'),
]