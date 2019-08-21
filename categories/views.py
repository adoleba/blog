from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from categories.models import Category
from posts.models import Post


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created')
    return render(request, 'users/user_posts.html', {'category': category, 'posts': posts})
