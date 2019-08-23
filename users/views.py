from django.contrib.auth.models import User
from django.core.paginator import Paginator
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
    queryset = Post.objects.filter(author=user).order_by('-created')
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    page_add_1 = posts.number + 1
    page_add_2 = posts.number + 2
    page_sub_1 = posts.number - 1
    page_sub_2 = posts.number - 2
    penult_page = posts.paginator.num_pages - 1

    return render(request, 'users/user_posts.html', {'posts': posts, 'user': user, 'photo': photo,
                                                     'page_add_1': page_add_1, 'page_sub_1': page_sub_1,
                                                     'page_add_2': page_add_2, 'page_sub_2': page_sub_2,
                                                     'penult_page': penult_page})
