from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'location'

urlpatterns = [
    path('locationdetail/', views.location_detail, name='location-detail'),
    path('bins/<int:pk>/', views.bin_pic, name='bin-pic'),  # pk 값에 따라 해당 수거함 사진 불러올 수 있도록 - 추가조치 필요
    path('etcinfo/', views.etc_info, name='etc-info'),
    path('etcinfo/clothing/', views.clothing_info, name='clothing-info'),
    path('etcinfo/battery/', views.battery_info, name='battery-info'),
    path('etcinfo/recycling/', views.recycling_info, name='recycling-info'),
    path('etcinfo/foodwaste/', views.foodwaste_info, name='foodwaste-info'),
    path('etcinfo/general/', views.general_info, name='general-info'),
    path('etcinfo/smallE/', views.smallE_info, name='smallE-info'),
    path('etcinfo/bigE/', views.bigE_info, name='bigE-info'),
    path('etcinfo/lamp/', views.lamp_info, name='lamp-info'),
    path('etcinfo/oil/', views.oil_info, name='oil-info'),
    path('etcinfo/furniture/', views.furniture_info, name='furniture-info'),
]