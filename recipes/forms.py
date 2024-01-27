from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    required_css_class = 'required-class'
    name = forms.CharField(help_text="This field is required")
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
            # self.fields[my_data['placeholder'][str(field)]].widget.attrs.update(
            #     my_data['placeholder']
            # )

class RecipeIngredientForm(forms.ModelForm):
    # ingredient_form_class = 'ingridient-form'
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
