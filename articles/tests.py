from django.test import TestCase
from .models import Article
# Create your tests here.
class ArticleModelTests(TestCase):
    def setUp(self):
        self.number_of_articles = 5
        for i in range(0,self.number_of_articles):
            Article.objects.create(title="Hello World", content="Something")


    def test_articles_number(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_first_slug(self):
        qs = Article.objects.first()
        slug = qs.slug
        self.assertTrue(slug, "hello-world")

    def test_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact="hello-world")
        for obj in qs:
            slug = obj.slug
            self.assertNotEqual(slug, "hello-world")

    def test_slugify_instance_method(self):

        qs = Article.objects.values_list("slug",flat=True)
        slug_list = list(set(qs))
        self.assertEqual(len(qs), len(slug_list))
