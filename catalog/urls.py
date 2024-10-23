from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('home/', views.show_home, name='show_home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>', views.product_detail, name='product')
]
