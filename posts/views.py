from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect

from categories.models import Category
from comments.forms import CommentForm
from comments.models import PostComment
from core.views import get_posts
from posts.models import Post


def index(request):
    head_post = Post.objects.filter(status='published').filter(published__lte=datetime.now()).last()
    head_post_categories = head_post.category.all()
    all_categories = Category.objects.all()

    posts = Post.objects.filter(status='published').filter(published__lte=datetime.now()).order_by('-published')[1:]

    ctx = get_posts(request, queryset=posts)
    return render(request, 'posts/index.html',
                  {'head_post': head_post, 'head_post_categories': head_post_categories,
                   'all_categories': all_categories, **ctx})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', published__year=year,
                             published__month=month, published__day=day)
    post_categories = post.category.all()
    post_comments = post.comments.filter(parent__isnull=True).order_by('-created')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_obj = PostComment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj

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

    return render(request, 'posts/post_detail.html', {'post': post, 'post_categories': post_categories,
                                                      'comment_form': comment_form, 'post_comments': post_comments,
                                                      'previous_post': previous_post, 'next_post': next_post})
