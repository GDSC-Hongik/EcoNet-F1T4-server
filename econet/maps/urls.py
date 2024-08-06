from django.urls import path
from .views import naver_map_data, bin_list, district_list, bin_detail, create_picture, create_info

urlpatterns = [
    path('', naver_map_data, name='naver_map_data'),
    path('bins/', bin_list, name='bin_list'),
    path('districts/', district_list, name='district_list'),
    path('<int:pk>/', bin_detail, name='bin_detail'),
    path('<int:pk>/pic_upload/', create_picture, name='create_picture'),
    path('<int:pk>/info_upload/', create_info, name='create_info')
]