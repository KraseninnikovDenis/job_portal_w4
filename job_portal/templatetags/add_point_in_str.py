from django import template

register = template.Library()


@register.filter
def add_point_in_str(string):
    return string.replace(',', ' •')
