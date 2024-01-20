from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse
from .utils import slugify_instance_title

# Create your models here.
class ArticleSearchQuery(models.QuerySet):
    def search(self,query=None):
        if query is not None:
            lookup = Q(title__icontains=query) | Q(content__icontains=query)
            return self.filter(lookup)
        else:
            return self.none()

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleSearchQuery(self.model, using=self._db)
    def search(self,query=None):
        return self.get_queryset().search(query=query)


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True,blank=True,auto_now_add=False, auto_now=False)
    objects = ArticleManager()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})

def article_pre_save(instance, **kwargs):
    slug = slugify(instance.title)
    if instance.slug is None or slug != instance.slug:
        slugify_instance_title(instance)
pre_save.connect(article_pre_save, sender=Article)

def article_post_save(created, instance, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
post_save.connect(article_post_save, sender=Article)
