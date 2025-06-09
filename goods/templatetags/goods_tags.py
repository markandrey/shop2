from django.utils.http import urlencode
from django import template
from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)  # все контекстные переменные из вьюшки (context, request) попадут в context
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)  # добавляем к запросу, который был на странице новые аргументы
    return urlencode(query)
