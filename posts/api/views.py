from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.api.serializers import PostListSerializer, PostDetailSerializer
from posts.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
