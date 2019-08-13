from django.urls import path

from posts.views import index, post_detail, posts_from_category

app_name = 'post'

urlpatterns = [
    path('', index),
    path('<int:year>/<int:month>/<int:day>/<slug>/', post_detail, name='post_detail'),

]