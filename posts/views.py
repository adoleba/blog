from django.shortcuts import render, get_object_or_404
from posts.models import Post


def index(request):
    posts = Post.objects.filter(status='published').order_by('-published')
    return render(request, 'posts/index.html',
                  {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', published__year=year,
                             published__month=month, published__day=day)
    categories = post.category.all()
    return render(request, 'posts/post_detail.html', {'post': post, 'categories': categories})


def posts_from_category():
    pass
