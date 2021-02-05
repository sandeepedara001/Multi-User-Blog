from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(PostListView.as_view()), name='blog-home' ),
    path('user/<str:username>', login_required(UserPostListView.as_view()), name='user-posts' ),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post-detail'),
    path('post/new/', login_required(PostCreateView.as_view()), name='post-create'),
    path('post/<int:pk>/update/', login_required(PostUpdateView.as_view()), name='post-update'),
    path('post/<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='search'),
]
