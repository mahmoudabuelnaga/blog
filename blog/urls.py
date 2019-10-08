from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
    UserPostListView,
    PostListAPIView,
    PostDetailAPIView,
)


urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name = 'user-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name='blog-about'),
    path('api/post/', PostListAPIView.as_view(), name="post-list-api"),
    path('api/post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail-api'),
]
