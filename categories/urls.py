from django.urls import path

from categories.views import category_posts

app_name = 'category'

urlpatterns = [
    path('<slug>/', category_posts, name='category_posts'),
]