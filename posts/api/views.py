from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.api.serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateDestroySerializer
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


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateDestroySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
