from django import template

register = template.Library()


@register.simple_tag
def subtraction(current_page, value):
    return current_page - value
