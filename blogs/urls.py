from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('blog/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('blog/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete')
]
