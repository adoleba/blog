from rest_framework.serializers import ModelSerializer

from categories.models import Category


class CategoriesListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

