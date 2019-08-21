from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from posts.models import Post
from users.models import UserProfile


def user_profile(request, user):
    userprofile = UserProfile.objects.filter(user__username=user)
    for field in userprofile:
        about = field.about_user
        intro = field.intro_user
        photo = field.photo
        user = field.user
    return render(request, 'users/user_profile.html',
                  {'userprofile': userprofile, 'about': about, 'intro': intro, 'photo': photo, 'user': user})


def user_posts(request, user):
    userprofile = UserProfile.objects.filter(user__username=user)
    for field in userprofile:
        user = field.user
        photo = field.photo
    posts = Post.objects.filter(author=user)
    return render(request, 'users/user_posts.html', {'posts': posts, 'user': user, 'photo': photo})
