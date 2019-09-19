from rest_framework.serializers import ModelSerializer

from comments.models import PostComment


class PostCommentListSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['post', 'author_name', 'created', 'parent']
