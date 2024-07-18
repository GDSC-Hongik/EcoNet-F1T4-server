from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='board'),
    #내모임 게시판
    path('mygathering/', views.index, name='mygathering'),
    path('mygathering_detail/', views.index, name='mygathering_detail'),
    path('mygathering_create/', views.index, name='mygathering_create'),

    #자유게시판
    path('public/', views.index, name='public'),
    path('public_detail/', views.index, name='public_detail'),
    path('public_create/', views.index, name='public_create'),

    #모임게시판
    path('gathering/', views.index, name='gathering'),
    path('gathering_detail/', views.index, name='gathering_detail'),
    path('gathering_create/', views.index, name='gathering_create'),

    #챌린지 게시판
    path('challenge/', views.index, name='challenge'),

    #스크랩한 글
    path('scrap/', views.index, name='scrap'),
    

    

]
