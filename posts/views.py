from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from comments.forms import CommentForm


def index(request):
    queryset = Post.objects.filter(status='published').filter(published__lte=datetime.now()).order_by('-published')
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
                   'page_sub_2': page_sub_2, 'penult_page': penult_page})


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

    return render(request, 'posts/post_detail.html', {'post': post, 'categories': categories,
                                                      'comment_form': comment_form, 'comments': comments})
