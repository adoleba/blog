from django import template
from categories.models import Category

register = template.Library()


@register.inclusion_tag('navbar.html')
def nav_categories():
    return {'nav_categories': Category.objects.all()}

