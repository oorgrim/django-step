from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    """Проверяет, равно ли количество элементов в value числу arg"""
    return len(value) == int(arg)
