from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from categories.models import Category
from posts.models import Post


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    queryset = Post.objects.filter(category=category).filter(published__lte=datetime.now()).order_by('-created')
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    page_add_1 = posts.number + 1
    page_add_2 = posts.number + 2
    page_sub_1 = posts.number - 1
    page_sub_2 = posts.number - 2
    penult_page = posts.paginator.num_pages - 1
    return render(request, 'categories/category_posts.html', {'category': category, 'posts': posts,
                                                              'page_add_1': page_add_1, 'page_sub_1': page_sub_1,
                                                              'page_add_2': page_add_2, 'page_sub_2': page_sub_2,
                                                              'penult_page': penult_page})
