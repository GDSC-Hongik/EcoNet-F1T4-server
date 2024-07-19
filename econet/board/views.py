from django.shortcuts import render, get_object_or_404
from .models import Board, Post

# Create your views here.

def board_list(request):
    boards = Board.objects.all()  # 모든 게시판을 조회
    return render(request, 'board_list.html', {'boards': boards})

def post_list(request, board_id):
    #id에 맞는 게시판 
    board = get_object_or_404(Board, id=board_id)
    # 필터 조건에서 'board' 사용
    posts = Post.objects.filter(board=board)
    return render(request, 'post_list.html', {'board': board, 'posts': posts})