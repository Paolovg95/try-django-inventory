from django.urls import path
from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_create_view,
    recipe_update_view,
    recipe_hx_detail_view,
    recipe_ingredient_hx_update_view
)

app_name = "recipes"
urlpatterns = [
    path('', recipe_list_view, name='recipes'),
    path('create/', recipe_create_view, name='create'),
    path('hx/<int:id>/', recipe_hx_detail_view, name='hx-detail'),
    path('hx/<int:parent_id>/ingredient/<int:id>/', recipe_ingredient_hx_update_view, name='hx-ingredient-detail'),
    path('hx/<int:parent_id>/ingredient/', recipe_ingredient_hx_update_view, name='hx-ingredient-create'),
    path('<int:id>/edit/', recipe_update_view, name='update'),
    path('<int:id>/', recipe_detail_view, name='detail')
]
