from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from blogs.models import Article


class ArticleCreateView(CreateView):
    """Класс для создания статьи"""
    model = Article
    template_name = "blogs/article_form.html"
    context_object_name = "article_create"

    fields = ('header', 'content')
    success_url = reverse_lazy('blogs:article_list')


class ArticleListView(ListView):
    """Класс для получения списка всех статей"""
    model = Article
    template_name = "blogs/article_list.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.filter(is_active=True)


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс для редактирования статьи"""
    model = Article
    template_name = "blogs/article_form.html"
    context_object_name = "article_create"
    permission_required = 'blogs.change_article_detail'
    fields = ('header', 'content')

    def get_success_url(self):
        return reverse('blogs:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    """Класс для удаления статьи"""
    model = Article
    template_name = "blogs/article_confirm_delete.html.html"
    context_object_name = "article_delete"
    permission_required = 'blogs.delete_article_detail'

    success_url = reverse_lazy("blogs:article_list")


class ArticleDetailView(DetailView):
    """Класс для представления полной информации о статье"""
    model = Article
    template_name = "blogs/article_detail.html"
    context_object_name = "article_detail"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()

        return self.object
