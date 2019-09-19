from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = ['url', 'title', 'category', 'author', 'status', 'published']


class PostDetailSerializer(ModelSerializer):
    main_photo = SerializerMethodField()
    thumbnail_photo = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'sub_title',
            'slug',
            'category',
            'created',
            'published',
            'status',
            'main_photo',
            'thumbnail_photo',
            'intro',
            'body',
            'comments',
        ]

    def get_main_photo(self, obj):
        try:
            main_photo = obj.main_photo.url
        except:
            main_photo = None
        return main_photo

    def get_thumbnail_photo(self, obj):
        try:
            thumbnain_photo = obj.thumbnail_photo.url
        except:
            thumbnain_photo = None
        return thumbnain_photo
