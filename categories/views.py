from datetime import datetime

from django.shortcuts import render, get_object_or_404

from categories.models import Category
from core.views import get_posts
from posts.models import Post


def category_posts(request, slug):
    post_category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    posts = Post.objects.filter(category=post_category).filter(published__lte=datetime.now()).order_by('-created')

    ctx = get_posts(request, queryset=posts)

    return render(
        request, 'categories/category_posts.html',
        {'post_category': post_category, 'categories': categories, **ctx}
    )
