from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Наполняем таблицу категории данными о категории
        category, _ = Category.objects.get_or_create(name='Какое-то название', description='И какое-то описание')

        # А также наполняем продукты категории
        products = [
            {'name': 'Какое-то имя продукта', 'description': 'Какое-то описание', 'category': category, 'price': 23},
            {'name': 'Также какое-то имя', 'description': 'Его какое-то описание', 'category': category, 'price': 44},
        ]

        # Выполняем команду циклом заполнения таблицы продуктов
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
