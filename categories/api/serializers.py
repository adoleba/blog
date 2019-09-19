from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField, PrimaryKeyRelatedField, StringRelatedField, \
    HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from categories.models import Category
from posts.models import Post

category_detail_url = HyperlinkedIdentityField(
    view_name='categories-api:detail',
    lookup_field='slug'
)


class CategoriesListSerializer(ModelSerializer):
    url = category_detail_url
    posts_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'url', 'posts_count']

    def get_posts_count(self, obj):
        return obj.posts.count()


class CategoryDetailSerializer(ModelSerializer):
    photo = SerializerMethodField()
    posts = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='posts-api:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = [
            'name',
            'photo',
            'posts',
        ]

    def get_photo(self, obj):
        try:
            photo = obj.photo.url
        except:
            photo = None
        return photo

    def get_posts(self, obj):
        a = obj.name
        return Post.objects.filter(category__name=a)
