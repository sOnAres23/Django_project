from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.conf import settings

from catalog.models import Product

base_dir = settings.BASE_DIR


def show_home(request: HttpRequest):
    """Обрабатывает запрос и возвращает html-страницу"""
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'products': products}

        return render(request, "catalog/home.html", context=context)


def show_contacts(request: HttpRequest):
    """Обрабатывает запрос и возвращает html-страницу"""
    if request.method == 'GET':
        return render(request, "catalog/contacts.html")


def contacts(request: HttpRequest):
    """Обрабатываем форму и возвращаем ответ"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        write_in_file = (f"\nИмя пользователя: {name}\n"
                         f"Телефон пользователя: {phone}\n"
                         f"Его сообщение: {message}\n")
        with open(r"C:\Users\Amd\Desktop\SkyPro\Messages.txt", "a", encoding="utf-8") as file:
            file.write(write_in_file)
        # А здесь мы просто возвращаем простой ответ пользователю на сайте:
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product_detail(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context=context)
