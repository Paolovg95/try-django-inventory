from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(null=True)
    content = models.TextField(null=True)
