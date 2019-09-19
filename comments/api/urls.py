from django.urls import path


from comments.api.views import PostCommentListAPIView
app_name = 'comments'

urlpatterns = [
    path('', PostCommentListAPIView.as_view(), name='list')
    ]
