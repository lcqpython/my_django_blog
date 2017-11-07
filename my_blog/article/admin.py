from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'category')

admin.site.register(Article, ArticleAdmin)
