from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm
from django.forms import modelformset_factory
from django.http import HttpResponse, Http404
# Create your views here.

@login_required
def recipe_list_view(request):
    recipes = Recipe.objects.filter(user=request.user)
    context = {
        'recipes' : recipes
    }
    return render(request, "recipes/list.html", context)

@login_required
def recipe_detail_view(request, id=None):
    # recipe = Recipe.objects.filter(id=id)
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'recipe': recipe
    }
    return render(request, "recipes/detail.html", context)

@login_required
def recipe_hx_detail_view(request, id=None):
    # recipe = Recipe.objects.filter(id=id)
    # recipe = get_object_or_404(Recipe, id=id, user=request.user)
    try:
        recipe = Recipe.objects.get(id=id, user=request.user)
    except:
        recipe = None
    if recipe is None:
        return HttpResponse("Not found.")
    context = {
        'recipe': recipe
    }
    return render(request, "recipes/partials/detail.html", context)
@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)

@login_required
def recipe_update_view(request, id=None):
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=recipe)
    RecipeIngredientFormSet = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=0)
    qs = recipe.recipeingredient_set.all()
    formset = RecipeIngredientFormSet(request.POST or None, queryset=qs)
    context = {
        'form': form,
        'formset': formset,
        'recipe': recipe
    }
    if form.is_valid():
        form.save()
        context['message'] = "Data is saved."
    if request.htmx:
        return render(request, "recipes/partials/form.html", context)
    return render(request, "recipes/create-update.html", context)

@login_required
def recipe_ingredient_hx_update_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not found.")
    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'object': instance
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['instance'] = new_obj
        return render(request, "recipes/partials/ingredient-inline.html", context)

    return render(request, "recipes/partials/ingredient-form.html", context)
