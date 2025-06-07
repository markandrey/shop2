from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "Домашняя",
        "content": 'Магазин - "Море интерьер-стиля"',
        "categories": categories,
        }
    return render(request, "shop_base/index.html", context)


def about(request) -> HttpResponse:
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": """
            DAMASK - это команда профессиональных дизайнеров, технологов, швей, замерщиков, установщиков,
            которые уже более 15 лет создают уют и красоту в жилых и общественных помещениях.

            Самая популярная наша услуга — это пошив штор на заказ.
            Будьте уверены, что готовые изделия полностью отразят первоначальную задумку, и вы получите именно те шторы,
            о которых мечтали. Качество нашего пошива полностью соответствует премиальному уровню тканей.""",
        }
    return render(request, "shop_base/about.html", context)
