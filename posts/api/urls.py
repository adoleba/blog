from django.urls import path


from posts.api.views import PostListAPIView, PostDetailAPIView
app_name = 'posts'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<slug>/', PostDetailAPIView.as_view(), name='detail')
    ]
