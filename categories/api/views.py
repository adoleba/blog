from rest_framework.generics import ListAPIView

from categories.api.serializers import CategoriesListSerializer
from categories.models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoriesListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        return queryset_list
