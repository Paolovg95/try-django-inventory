from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(null=True,blank=True,auto_now_add=False, auto_now=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

def slugify_instance_title(instance, save=False):
    instance.slug = slugify(instance.title)
    if save:
        instance.save()

def article_pre_save(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    if instance.slug is None or slug != instance.slug:
        slugify_instance_title(instance)
pre_save.connect(article_pre_save, sender=Article)

def article_post_save(created, instance, sender, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
post_save.connect(article_post_save, sender=Article)
