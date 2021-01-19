from django.urls import path

from comments.api.views import PostCommentListAPIView, PostCommentDetailAPIView
app_name = 'comments'

urlpatterns = [
    path('', PostCommentListAPIView.as_view(), name='list'),
    path('<pk>/', PostCommentDetailAPIView.as_view(), name='detail')
    ]
