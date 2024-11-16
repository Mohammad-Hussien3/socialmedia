from django.urls import path
from . import views

urlpatterns = [
    path('addpost/', views.AddPost.as_view(), name='addPost'),
    path('addcomment/', views.AddComment.as_view(), name='addComment'),
    path('mention/', views.CreateMention.as_view(), name='createMention'),
    path('react/', views.AddReaction.as_view(), name='addReaction'),
    path('marknotificationastrue/<int:id>/', views.MarkNotificationAsRead.as_view(), name='markNotificationAsTrue'),
    path('getmynotifications/', views.GetMyNotifications.as_view(), name='getMyNotifications'),
]