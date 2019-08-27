from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from categories.models import Category
from posts.models import Post
from comments.forms import CommentForm


def index(request):
    head_post = Post.objects.filter(status='published').filter(published__lte=datetime.now()).last()
    head_post_categories = head_post.category.all()
    all_categories = Category.objects.all()

    queryset = Post.objects.filter(status='published').filter(published__lte=datetime.now()).order_by('-published')[1:]
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    page_add_1 = posts.number + 1
    page_add_2 = posts.number + 2
    page_sub_1 = posts.number - 1
    page_sub_2 = posts.number - 2
    penult_page = posts.paginator.num_pages - 1
    return render(request, 'posts/index.html',
                  {'posts': posts, 'page_add_1': page_add_1, 'page_sub_1': page_sub_1, 'page_add_2': page_add_2,
                   'page_sub_2': page_sub_2, 'penult_page': penult_page, 'head_post': head_post,
                   'head_post_categories': head_post_categories, 'all_categories': all_categories})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', published__year=year,
                             published__month=month, published__day=day)
    categories = post.category.all()
    comments = post.comments.all().order_by('-created')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return redirect(request.path)
    else:
        comment_form = CommentForm()

    try:
        previous_post = post.get_previous_by_published()
    except post.DoesNotExist:
        previous_post = post

    try:
        next_post = post.get_next_by_published()
    except post.DoesNotExist:
        next_post = post

    return render(request, 'posts/post_detail.html', {'post': post, 'categories': categories,
                                                      'comment_form': comment_form, 'comments': comments,
                                                      'previous_post': previous_post, 'next_post': next_post})
