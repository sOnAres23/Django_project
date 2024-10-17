from django.contrib import admin
from .models import Category, Product

# создали Админку в виде Суперользователя
# и Классы для отображения моделей в админке


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Категории в админке"""
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('id', 'name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Продуктов в админке"""
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('name', 'price', 'category',)
    search_fields = ('id', 'name', 'description')
