from django.urls import path
from .views import DistrictListView, naver_map

urlpatterns = [
    path("", DistrictListView.as_view(), name='district-list'),
    path("map/", naver_map, name='naver_map'),
]