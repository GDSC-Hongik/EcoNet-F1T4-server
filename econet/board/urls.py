from django.urls import path
from . import views

urlpatterns = [
    #게시판 목록 페이지
    path('', views.board_list, name='board_list'),

    #각 게시판의 게시글 목록 페이지
    path('<int:board_id>/', views.post_list, name='post_list'),

    #게시글 작성 페이지
    path('<int:board_id>/create/', views.create_post, name='post_create'),

    #게시글 상세 페이지
    path('<int:board_id>/<int:post_id>/', views.post_detail, name='post_detail'),

    #게시글 수정 페이지
    path('<int:board_id>/<int:post_id>/edit/', views.edit_post, name='post_edit'),

    #게시글 삭제 페이지
    path('<int:board_id>/<int:post_id>/delete/', views.delete_post, name='post_delete'),



]
