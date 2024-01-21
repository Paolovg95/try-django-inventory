from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    fields = ['name', 'quantity', 'unit', 'directions', 'quantity_as_float']
    readonly_fields = ['quantity_as_float']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('name', 'description', 'id')
    raw_id_fields = ('user', )
