from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLE


class CatalogService:

    @staticmethod
    def get_products_from_cache():
        """Функция, которая получает данные по продуктам из кэша, если кэш пуст, то получает данные из БД"""
        if not CACHE_ENABLE:
            return Product.objects.all()
        key = 'products_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products, 60)
        return products

    @staticmethod
    def get_products_by_category(category_id):
        """Функция, которая получает данные по продуктам категории из кэша, если кэш пуст, то получает данные из БД"""
        if not CACHE_ENABLE:
            return Product.objects.filter(category_id=category_id)
        key = f'products_by_category_{category_id}'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60)
        return products
