from django.urls import path
from .views import bin_list, bin_detail, create_picture, create_info

urlpatterns = [
    path('', bin_list, name='bin_list'),
    path('<int:pk>/', bin_detail, name='bin_detail'),
    path('<int:pk>/pic_upload/', create_picture, name='create_picture'),
    path('<int:pk>/info_upload/', create_info, name='create_info')
]