from django.urls import path
from . import views

urlpatterns = [
    # Posts
    path('addpost/', views.AddPost.as_view(), name='addPost'),
    path('getmyposts/<int:id>/', views.GetMyPosts.as_view(), name='getMyPosts'),

    # Comments
    path('addcomment/', views.AddComment.as_view(), name='addComment'),

    # Mentions
    path('mention/', views.CreateMention.as_view(), name='createMention'),

    # Reactions
    path('react/', views.AddReaction.as_view(), name='addReaction'),

    # Notifications
    path('marknotificationastrue/<int:id>/', views.MarkNotificationAsRead.as_view(), name='markNotificationAsTrue'),
    path('getmynotifications/<int:id>/', views.GetMyNotifications.as_view(), name='getMyNotifications'),
]