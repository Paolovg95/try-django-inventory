from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True,blank=True,auto_now_add=False, auto_now=False)
