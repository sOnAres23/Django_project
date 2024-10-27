from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

base_dir = settings.BASE_DIR


class ProductCreateView(CreateView):
    """Класс предаставленный пользователю для создания нового продукта"""
    model = Product
    template_name = 'catalog/product_form.html'
    context_object_name = "product_create"

    fields = ('name', 'description', 'price', 'category', 'picture')
    success_url = reverse_lazy('catalog:show_home')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    context_object_name = "product_update"

    fields = ('name', 'description', 'price', 'category', 'picture')

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class CatalogListView(ListView):
    """Класс для представления главной страницы каталога"""
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CatalogDetailView(DetailView):
    """Класс для представления страницы полной информации о товаре"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class CatalogTemplateView(TemplateView):
    """Класс для представления страницы обратной связи"""
    template_name = "catalog/contacts.html"

    def post(self, request):
        if self.request.method == 'POST':
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

# def show_home(request: HttpRequest):
#     """Обрабатывает запрос и возвращает html-страницу"""
#     if request.method == 'GET':
#         products = Product.objects.all()
#         context = {'products': products}
#
#         return render(request, "catalog/home.html", context=context)
#
#
# def show_contacts(request: HttpRequest):
#     """Обрабатывает запрос и возвращает html-страницу"""
#     if request.method == 'GET':
#         return render(request, "catalog/contacts.html")
#
#
# def contacts(request: HttpRequest):
#     """Обрабатываем форму и возвращаем ответ"""
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         write_in_file = (f"\nИмя пользователя: {name}\n"
#                          f"Телефон пользователя: {phone}\n"
#                          f"Его сообщение: {message}\n")
#         with open(r"C:\Users\Amd\Desktop\SkyPro\Messages.txt", "a", encoding="utf-8") as file:
#             file.write(write_in_file)
#         # А здесь мы просто возвращаем простой ответ пользователю на сайте:
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'catalog/contacts.html')
#
#
# def product_detail(request: HttpRequest, pk: int):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context=context)
