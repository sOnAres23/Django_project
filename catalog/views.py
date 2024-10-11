from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def show_home(request: HttpRequest):
    """функция обрабатывает запрос и возвращает html-страницу"""
    if request.method == 'GET':
        return render(request, "catalog/home.html")


def show_contacts(request: HttpRequest):
    """обрабатываем запрос и возвращаем html-страницу"""
    if request.method == 'GET':
        return render(request, "catalog/contacts.html")


def contacts(request: HttpRequest):
    """Обрабатываем форму и возвращаем ответ"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')
