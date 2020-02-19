from django.core.paginator import Paginator


def get_posts(request, queryset):
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ctx = {
        'posts': posts,
        'page_add_1': posts.number + 1,
        'page_add_2': posts.number + 2,
        'page_sub_1': posts.number - 1,
        'page_sub_2': posts.number - 2,
        'penult_page': posts.paginator.num_pages - 1
        }
    return ctx
