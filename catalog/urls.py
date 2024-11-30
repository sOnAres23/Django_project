from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'catalog'

urlpatterns = [
    path('home/', cache_page(60)(views.CatalogListView.as_view()), name='show_home'),
    path('contacts/', views.CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(views.CatalogDetailView.as_view()), name='product'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
