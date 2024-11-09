from django.db import models


class Category(models.Model):
    """Модель создания таблицы Категории в БД"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True)

    def __str__(self):
        return f"Категория: {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    """Модель создания таблицы Продукты в БД"""
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите название продукта')
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, help_text='Введите описание')
    picture = models.ImageField(upload_to='catalog/photos/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория', help_text='Выберите предложенную категорию')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}$."

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at']
