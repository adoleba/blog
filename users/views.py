from datetime import datetime

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from posts.models import Post
from users.models import User


def user_profile(request, username):
    userprofile = User.objects.filter(username=username)
    for field in userprofile:
        about = field.about_user
        intro = field.intro_user
        photo = field.photo
        username = field.username
    return render(request, 'users/user_profile.html',
                  {'userprofile': userprofile, 'about': about, 'intro': intro, 'photo': photo, 'username': username})


def user_posts(request, username):
    userprofile = User.objects.filter(username=username)
    for field in userprofile:
        username = field.username
        photo = field.photo
        number = field.id
    queryset = Post.objects.filter(author=number).filter(published__lte=datetime.now()).order_by('-created')
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    page_add_1 = posts.number + 1
    page_add_2 = posts.number + 2
    page_sub_1 = posts.number - 1
    page_sub_2 = posts.number - 2
    penult_page = posts.paginator.num_pages - 1

    return render(request, 'users/user_posts.html', {'posts': posts, 'username': username, 'photo': photo,
                                                     'page_add_1': page_add_1, 'page_sub_1': page_sub_1,
                                                     'page_add_2': page_add_2, 'page_sub_2': page_sub_2,
                                                     'penult_page': penult_page})
