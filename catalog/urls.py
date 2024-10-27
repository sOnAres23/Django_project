from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('home/', views.CatalogListView.as_view(), name='show_home'),
    path('contacts/', views.CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', views.CatalogDetailView.as_view(), name='product')
]
