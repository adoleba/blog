from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from users.models import UserProfile


def user_profile(request, username):
    userprofile = get_object_or_404(User, username=request.user)
    return render(request, 'users/user_profile.html',
                  {'userprofile': userprofile})
