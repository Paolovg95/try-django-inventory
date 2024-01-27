from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recipe name'}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            my_data = {
                'class': 'form-control',
                'placeholder': f'Recipe {str(field)}'
            }
            self.fields[str(field)].widget.attrs.update(
                my_data
            )

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
