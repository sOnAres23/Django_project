from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at', 'updated_at', "owner"]


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['is_published', 'owner']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка для отображения подсказки для поля 'name'
        self.fields['name'].widget.attrs.update({
            'placeholder': 'название '
        })

        # Настройка для отображения подсказки для поля 'description'
        self.fields['description'].widget.attrs.update({
            'placeholder': 'описание без спам слов'
        })

    def clean(self):
        """Валидация полей имени и описания на отсутствие запрещенных слов"""
        list_wrong_words = ["казино", "бомба", "ставки", "дешево",
                            "бесплатно", "обман", "полиция", "радар"]
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        for word in list_wrong_words:
            if word in name.lower():
                self.add_error('name', f'К сожалению, ваш продукт не может содержать слово: "{word}" :(')
            if word in description.lower():
                self.add_error('description', f'К сожалению, ваш продукт не может содержать слово: "{word}" :(')

    def clean_price(self):
        """Валидация поля цены, что цена продукта не может быть отрицательной"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной!')
        return price

    def clean_photo(self):
        """Валидация поля фотографии, чтобы фото продукта было правильного разрешения и размера"""
        image = self.cleaned_data.get('photo')

        # Проверка формата файла
        if image:
            if not (image.name.endswith('.jpg') or image.name.endswith('.jpeg') or image.name.endswith('.png')):
                raise ValidationError("Формат файла должен быть JPEG или PNG.")

            # Проверка размера файла
            if image.size > 10 * 1024 * 1024:
                raise ValidationError("Размер файла не должен превышать 10 МБ.")
        return image
