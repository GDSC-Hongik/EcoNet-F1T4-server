from django.urls import path
from . import views

urlpatterns = [
    #게시판 목록 페이지
    path('board/', views.board_list, name='board_list'),

    #각 게시판의 게시글 목록 페이지
    path('board/<int:board_id>/', views.post_list, name='post_list'),

    

]
