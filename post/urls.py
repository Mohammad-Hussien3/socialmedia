from django.urls import path
from . import views

urlpatterns = [
    # Posts
    path('addpost/', views.AddPost.as_view(), name='addPost'),
    path('getmyposts/<int:id>/', views.GetMyPosts.as_view(), name='getMyPosts'),
    path('trendingposts/<int:id>/', views.TrendingPosts.as_view(), name='trendingPosts'),

    # Comments
    path('addcomment/', views.AddComment.as_view(), name='addComment'),
    path('getmycomments/<int:id>/', views.GetMyComments.as_view(), name='getMyComments'),
    path('getpostcomments/<int:postId>/', views.GetPostCommetns.as_view(), name='getPostComments'),

    # Mentions
    path('mention/', views.CreateMention.as_view(), name='createMention'),

    # Reactions
    path('react/', views.AddReaction.as_view(), name='addReaction'),

    # Notifications
    path('marknotificationastrue/<int:id>/', views.MarkNotificationAsRead.as_view(), name='markNotificationAsTrue'),
    path('getmynotifications/<int:id>/', views.GetMyNotifications.as_view(), name='getMyNotifications'),
    path('getnotification/<int:id>/', views.GetNotification.as_view(), name='getOneNotification'),

    # Story
    path('addstory/', views.AddStory.as_view(), name='addStory'),
]