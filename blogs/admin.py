from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Категории в админке"""
    list_display = ('id', 'header', 'content', 'picture',)
    list_filter = ('header',)
    search_fields = ('id', 'header',)
