from django.urls import path
from . import views

urlpatterns = [
    path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('addcomment/', views.AddComment.as_view(), name='addcomment'),
]