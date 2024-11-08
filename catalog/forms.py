from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name in self.fields.keys():  # получаем название полей
            self.fields[field_name].widget.attrs.update({  # присваеваем значения полям на основании перебора
                'class': 'form-control',
                'placeholder': f"{field_name}",
            })

    def clean(self):
        """Валидация полей имени и описания на отсутствие запрещенных слов"""
        list_wrong_words = ["казино", "криптовалюта", "крипта", "биржа",
                            "дешево", "бесплатно", "обман", "полиция", "радар"]
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name or description in list_wrong_words:
            raise ValidationError('К сожалению, ваш продукт не может содержать такие слова:(')

    def clean_price(self):
        """Валидация поля цены, что цена продукта не может быть отрицательной"""
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной!')
        return price

# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for fild_name, fild in self.fields.items():
#             if isinstance(fild, BooleanField):
#                 fild.widget.attrs['class'] = "form-check-input"
#             else:
#                 fild.widget.attrs['class'] = "form-control"
