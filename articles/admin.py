from django.contrib import admin
from .models import Article

# admin.site.register(Article)
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','id')
