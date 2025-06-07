from django.urls import path
from shop_base import views


app_name = 'shop_base'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
