
from django.conf import settings
from django.db import models
from .validators import validate_unit_measure

User = settings.AUTH_USER_MODEL
# Create your models here.
"""
Global
    - Ingredients
    - Recipes
User
    - Recipes
        - Ingredients

"""

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, null=True)
    directions = models.TextField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, null=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, validators=[validate_unit_measure])
    directions = models.TextField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
