from rest_framework.fields import HiddenField
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser

from comments.api.serializers import PostCommentListSerializer, PostCommentDetailSerializer
from comments.api.permissions import IsAdminUserOrReadOnly
from comments.models import PostComment


class PostCommentListAPIView(ListAPIView):
    serializer_class = PostCommentListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostComment.objects.all()
        return queryset_list


class PostCommentDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = PostCommentDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = PostComment.objects.all()
    lookup_field = 'pk'

