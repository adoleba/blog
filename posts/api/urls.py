from django.urls import path

from posts.api.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView

app_name = 'posts'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<slug>/', PostDetailAPIView.as_view(), name='detail'),
    ]
