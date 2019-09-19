from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField, HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from comments.models import PostComment
from posts.api.serializers import PostDetailSerializer

comment_detail_url = HyperlinkedIdentityField(
    view_name='comments-api:detail',
    lookup_field='pk'
)


class PostCommentListSerializer(ModelSerializer):
    url = comment_detail_url
    reply_count = SerializerMethodField()
    post = HyperlinkedRelatedField(
        read_only=True,
        view_name='posts-api:detail',
        lookup_field='slug'
    )

    class Meta:
        model = PostComment
        fields = ['author_name', 'url', 'reply_count', 'post']

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()


class PostCommentChildSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            'author_name',
            'email',
            'body',
            'created',
        ]


class PostCommentDetailSerializer(ModelSerializer):
    post = HyperlinkedRelatedField(
        read_only=True,
        view_name='posts-api:detail',
        lookup_field='slug'
    )
    replies = SerializerMethodField()

    class Meta:
        model = PostComment
        fields = [
            'post',
            'author_name',
            'email',
            'body',
            'created',
            'parent',
            'replies',
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return PostCommentChildSerializer(obj.children(), many=True).data
        return None
