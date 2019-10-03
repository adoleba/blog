from django.urls import path

from users.views import user_profile, user_posts

app_name = 'users'

urlpatterns = [
    path('<username>/', user_profile, name='user_profile'),
    path('<username>/posts/', user_posts, name='user_posts'),
]
