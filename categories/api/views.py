from rest_framework.generics import ListAPIView, RetrieveAPIView

from categories.api.serializers import CategoriesListSerializer, CategoryDetailSerializer
from categories.models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoriesListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        return queryset_list


class CategoryDetailAPIView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'

