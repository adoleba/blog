from django.urls import path

from posts.views import index, post_detail

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug>/', post_detail, name='post_detail'),
]
