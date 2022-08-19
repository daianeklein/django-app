from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('<h1>Recipes</h1>')

def index(request):
    return render(request,'index.html')

def view_recipes_page(request):
    return render(request, 'recipes.html')

