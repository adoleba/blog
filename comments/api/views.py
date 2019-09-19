from rest_framework.generics import ListAPIView

from comments.api.serializers import PostCommentListSerializer
from comments.models import PostComment


class PostCommentListAPIView(ListAPIView):
    serializer_class = PostCommentListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostComment.objects.all()
        return queryset_list
