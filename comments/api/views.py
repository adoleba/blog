from rest_framework.generics import ListAPIView, RetrieveAPIView

from comments.api.serializers import PostCommentListSerializer, PostCommentDetailSerializer
from comments.models import PostComment


class PostCommentListAPIView(ListAPIView):
    serializer_class = PostCommentListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostComment.objects.all()
        return queryset_list


class PostCommentDetailAPIView(RetrieveAPIView):
    serializer_class = PostCommentDetailSerializer
    queryset = PostComment.objects.all()
    lookup_field = 'pk'
