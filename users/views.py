from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render

from core.views import get_posts
from posts.models import Post
from users.models import User


def user_profile(request, username):
    userprofile = User.objects.filter(username=username)
    ctx = {}
    for field in userprofile:
        ctx['about'] = field.about_user
        ctx['intro'] = field.intro_user
        ctx['photo'] = field.photo
        ctx['username'] = field.username
        ctx['first_name'] = field.first_name
        ctx['last_name'] = field.last_name
    return render(request, 'users/user_profile.html',
                  {'userprofile': userprofile, **ctx})


def user_posts(request, username):
    userprofile = User.objects.filter(username=username)
    for field in userprofile:
        username = field.username
        photo = field.photo
        number = field.id
    queryset = Post.objects.filter(author=number).filter(published__lte=datetime.now()).order_by('-created')

    ctx = get_posts(request, queryset=queryset)

    return render(request, 'users/user_posts.html', {'username': username, 'photo': photo, **ctx})
