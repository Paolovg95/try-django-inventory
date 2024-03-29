import pint
from django.conf import settings
from django.db import models
from .validators import validate_unit_measure
from .utils import number_str_to_float
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id} )
    def get_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id} )
    def get_edit_url(self):
        return reverse("recipes:update", kwargs={"id": self.id} )



class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True,null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_measure])
    directions = models.TextField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id
        }
        return reverse("recipes:hx-ingredient-detail", kwargs=kwargs)


    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement

    def to_mks(self):
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()

    def to_imperial(self):
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        quantity = self.quantity
        quantity_float, quantity_boolean = number_str_to_float(quantity)
        if quantity_boolean:
            self.quantity_as_float = quantity_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
