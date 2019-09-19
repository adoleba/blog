from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from categories.models import Category


category_detail_url = HyperlinkedIdentityField(
    view_name='categories-api:detail',
    lookup_field='slug'
)


class CategoriesListSerializer(ModelSerializer):
    url = category_detail_url

    class Meta:
        model = Category
        fields = ['name', 'url']


class CategoryDetailSerializer(ModelSerializer):
    photo = SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'name',
            'photo',
        ]

    def get_photo(self, obj):
        try:
            photo = obj.photo.url
        except:
            photo = None
        return photo