from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    fields = ['name', 'quantity', 'unit', 'directions']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('name', 'description', 'id')
    raw_id_fields = ('user', )
