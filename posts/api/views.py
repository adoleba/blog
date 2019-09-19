from rest_framework.generics import ListAPIView

from posts.api.serializers import PostListSerializer
from posts.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        return queryset_list
