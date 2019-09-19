from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField, StringRelatedField, SlugRelatedField, \
    HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from comments.models import PostComment
from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    comments_count = SerializerMethodField()
    author = SerializerMethodField()
    category = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Post
        fields = ['url', 'title', 'category', 'author', 'status', 'published', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        return obj.category.name


class PostDetailSerializer(ModelSerializer):
    category = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='categories-api:detail',
        lookup_field='slug'
    )

    main_photo = SerializerMethodField()
    thumbnail_photo = SerializerMethodField()
    author = SerializerMethodField()
    comments = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='body'
     )

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

    def get_comments(self, obj):
        obj_id = obj.id
        return PostComment.objects.filter(post_id=obj_id)

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        print(obj.name)
        category_name = obj.name
        return Post.objects.filter(category__name=category_name)
