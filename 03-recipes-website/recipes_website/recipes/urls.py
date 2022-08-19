from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('recipes', views.view_recipes_page, name = 'recipes'),
]
