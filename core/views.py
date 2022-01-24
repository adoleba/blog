from django.core.paginator import Paginator


def get_posts(request, queryset):
    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ctx = {
        'posts': posts,
        'current_page_plus_1': posts.number + 1,
        'current_page_plus_2': posts.number + 2,
        'current_page_minus_1': posts.number - 1,
        'current_page_minus_2': posts.number - 2,
        'penult_page': posts.paginator.num_pages - 1
        }
    return ctx
