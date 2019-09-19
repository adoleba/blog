from django.urls import path


from posts.api.views import PostListAPIView
app_name = 'posts'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list')
    ]
