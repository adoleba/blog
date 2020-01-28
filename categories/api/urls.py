from django.urls import path

from categories.api.views import CategoryListAPIView, CategoryDetailAPIView, CategoryCreateAPIView

app_name = 'categories'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='list'),
    path('create/', CategoryCreateAPIView.as_view(), name='create'),
    path('<slug>/', CategoryDetailAPIView.as_view(), name='detail')
    ]
