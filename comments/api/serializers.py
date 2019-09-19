from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from comments.models import PostComment


comment_detail_url = HyperlinkedIdentityField(
    view_name='comments-api:detail',
    lookup_field='pk'
)


class PostCommentListSerializer(ModelSerializer):
    url = comment_detail_url

    class Meta:
        model = PostComment
        fields = ['post', 'author_name', 'url']


class PostCommentDetailSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            'post',
            'author_name',
            'email',
            'body',
            'created',
            'parent',
        ]
