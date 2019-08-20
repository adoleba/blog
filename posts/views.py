from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post
from comments.forms import CommentForm


def index(request):
    posts = Post.objects.filter(status='published').order_by('-published')
    return render(request, 'posts/index.html',
                  {'posts': posts})


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


def posts_from_category():
    pass
