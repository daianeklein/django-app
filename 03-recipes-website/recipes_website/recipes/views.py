from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# def index(request):
#     return HttpResponse('<h1>Recipes</h1>')

def index(request):
    return render(request,'index.html')

def view_recipes_page(request):
    recipes = Recipe.objects.all()

    data_recipes = {
        'recipes' : recipes 
    }
    return render(request, 'recipes.html', data_recipes)

def view_recipes_details(request):
    return render(request, 'recipes_details.html')

