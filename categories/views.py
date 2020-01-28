from datetime import datetime

from django.shortcuts import render, get_object_or_404

from categories.models import Category
from core.views import get_posts
from posts.models import Post


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    queryset = Post.objects.filter(category=category).filter(published__lte=datetime.now()).order_by('-created')

    ctx = get_posts(request, queryset=queryset)

    return render(request, 'categories/category_posts.html', {'category': category, 'categories': categories, **ctx})
