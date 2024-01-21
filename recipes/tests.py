from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recipe, RecipeIngredient
from django.contrib.auth import get_user_model
# Create your tests here.


User = get_user_model()
class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user("test_user", password="abc123")

    def test_user_password(self):
        password = self.user_a.check_password("abc123")
        self.assertTrue(password)

class RecipeTestCase(TestCase):

    def setUp(self):
        self.user_b = User.objects.create_user("recipe_user", password="abc123")
        self.recipe_b = Recipe.objects.create(
            name="Beef Burrito",
            user = self.user_b,
        )
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe = self.recipe_b,
            name = "Chicken",
            quantity = "1",
            unit = "kg"
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_recipe_reverse_count(self):
        user = self.user_b
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(), 1)

    def test_recipe_forward_count(self):
        user = self.user_b
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),1)

    def test_recipe_ingredient_reverse(self):
        recipe =  self.recipe_b
        qs = recipe.recipeingredient_set.all()
        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredient_forward(self):
        recipe = self.recipe_b
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 1)

    def test_two_level_relation(self):
        user = self.user_b
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 1)

    def two_level_relation_via_recipe(self):
        user = self.user_b
        ids = user.recipe_set.all().values_list("id", flat=True)
        print(ids)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(), 1)

    def test_unit_validator_positive(self):
        ingredient = RecipeIngredient(
            recipe = self.recipe_b,
            name= "Salt",
            quantity = "1/8",
            unit = "gr"
        )
        ingredient.full_clean()

    def test_unit_validator_negative(self):
        invalid_unit = "blablanada"
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                recipe = self.recipe_b,
                name= "Salt",
                quantity = "1/8",
                unit = invalid_unit
            )
            ingredient.full_clean()
