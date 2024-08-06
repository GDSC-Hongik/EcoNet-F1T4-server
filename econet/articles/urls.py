from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('search/', views.search_articles, name='search_articles'),
]
