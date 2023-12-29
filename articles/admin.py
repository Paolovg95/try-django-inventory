from django.contrib import admin
from .models import Article

# admin.site.register(Article)
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(Article, ArticleAdmin)
