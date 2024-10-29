from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('add_article/', views.ArticleCreateView.as_view(), name='article_form'),
    path('blog/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete')
]
