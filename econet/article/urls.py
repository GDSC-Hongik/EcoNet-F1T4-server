from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='article'),
    path('starred/', views.index, name='starred'),
    path('article_detail/', views.index, name='article_detail'),
]
