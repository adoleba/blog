from django.urls import path

from users.views import user_profile, user_posts

app_name = 'users'

urlpatterns = [
    path('<user>/', user_profile, name='user_profile'),
    path('<user>/posts/', user_posts, name='user_posts'),
]
