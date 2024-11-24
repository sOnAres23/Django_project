import os
# get_object_or_404, redirect,
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from catalog.services import CatalogService


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания нового продукта"""
    model = Product
    template_name = 'catalog/product_form.html'
    context_object_name = "product_create"
    form_class = ProductForm
    success_url = reverse_lazy('catalog:show_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление продукта на сайт'
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования продукта"""
    model = Product
    template_name = 'catalog/product_form.html'
    context_object_name = "product_update"
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = self.request.user
        if user != product.owner:
            if not user.has_perm('catalog.change_product'):
                return HttpResponseForbidden("У вас нет прав для редактирования этого продукта!")
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        return ProductForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatalogListView(ListView):
    """Класс для представления главной страницы каталога"""
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        return CatalogService.get_products_from_cache()


class CatalogDetailView(DetailView):
    """Класс для представления полной информации о товаре"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:show_home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = self.request.user
        if user != product.owner:
            if not user.has_perm('catalog.delete_product'):
                return HttpResponseForbidden("У вас нет прав для удаления этого продукта!")
        return super().dispatch(request, *args, **kwargs)


class ProductsByCategoryView(ListView):
    template_name = 'catalog/category_products.html'
    context_object_name = "products"

    def get_queryset(self):
        # Получаем category_id из URL
        category_id = self.kwargs.get('category_id')
        return CatalogService.get_products_by_category(category_id=category_id)

    def get_context_data(self, **kwargs):
        """
        Добавляет информацию о категории в контекст.
        """
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get('category_name')
        context["products"] = self.get_queryset()
        return context


class CatalogTemplateView(TemplateView):
    """Класс для представления страницы обратной связи"""
    template_name = "catalog/contacts.html"

    def post(self, request):
        if self.request.method == 'POST':
            # Получение данных из формы
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            # Обработка данных (для примера, отправка email и запись в файл)
            send_mail(f'Письмо от пользователя: {name}', f'Сообщение: {message}, Телефон для связи: {phone}',
                      settings.EMAIL_HOST_USER, ['sergeyspisak@yandex.ru'])
            write_in_file = (f"\nИмя пользователя: {name}\n"
                             f"Телефон пользователя: {phone}\n"
                             f"Его сообщение: {message}\n")
            with open(f"{os.getenv('PATH_FILE')}", "a", encoding="utf-8") as file:
                file.write(write_in_file)
            # А здесь мы просто возвращаем простой ответ пользователю на сайте:
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return render(request, 'catalog/contacts.html')
