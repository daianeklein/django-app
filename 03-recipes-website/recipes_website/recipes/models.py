from django.db import models
from datetime import datetime

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    directions = models.TextField()
    prep = models.IntegerField()
    servings = models.CharField(max_length=20)
    date_recipe = models.DateTimeField(default=datetime.now, blank=True)
