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

def article_pre_save(sender, instance, *args, **kwargs):
    # print("instance", instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)
    # print("sender", sender)
    # print(kwargs)
pre_save.connect(article_pre_save, sender=Article)

def article_post_save(created, instance, sender, *args, **kwargs):
    if created:
        instance.slug = "Some sluuuuggg"
        instance.save()

post_save.connect(article_post_save, sender=Article)
