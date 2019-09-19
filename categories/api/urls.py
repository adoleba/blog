from django.urls import path


from categories.api.views import CategoryListAPIView
app_name = 'categories'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='list')
    ]
