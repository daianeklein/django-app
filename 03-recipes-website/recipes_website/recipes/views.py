from django.shortcuts import render, get_list_or_404, get_object_or_404
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

def view_recipes_details(request, recipes_id):
    recipe = get_object_or_404(Recipe, pk=recipes_id)

    show_recipe = {
        'recipe' : recipe
    }

    return render(request, 'recipes_details.html', show_recipe)

