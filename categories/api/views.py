from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from comments.api.permissions import IsAdminUserOrReadOnly
from categories.api.serializers import CategoriesListSerializer, CategoryDetailSerializer, \
    CategoryCreateUpdateDestroySerializer
from categories.models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoriesListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Category.objects.all()
        return queryset_list


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Category.objects.all()
    lookup_field = 'slug'


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateDestroySerializer
    permission_classes = [IsAdminUser]
