from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Номер телефона')
    username = forms.CharField(max_length=50, required=True, help_text='Введите ваш никнейм')
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number',
                  'country', 'password1', 'password2', 'avatar')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры!')
        return phone_number
