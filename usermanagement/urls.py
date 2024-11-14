from django.urls import path
from . import views

urlpatterns = [
    path('token/refresh/', views.TokenRefreshView.as_view(), name='refreshToken'),
    
    path('signup/', views.SignUp.as_view(), name='signUp'),
    path('logout/<int:id>/', views.LogOut.as_view(), name='logOut'),
    path('login/', views.LogIn.as_view(), name='logIn'),
    path('getusers/', views.GetUsers().as_view(), name='getUsers'),
    path('follow/<int:userId>/<int:userToFollowId>/', views.FollowUser.as_view(), name='followUser'),
    path('unfollow/<int:userId>/<int:userToUnfollowId>/', views.UnfollowUser.as_view(), name='unfollowUser'),
]