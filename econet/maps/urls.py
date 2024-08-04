from django.urls import path
from .views import bin_list, bin_detail

urlpatterns = [
    path('', bin_list, name='bin_list'),
    path('<int:pk>/', bin_detail, name='bin_detail'),
]