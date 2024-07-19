from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Board, Post

# Create your views here.

def board_list(request):
    boards = Board.objects.all()  # 모든 게시판을 조회
    return render(request, 'board/board_list.html', {'boards': boards})

def post_list(request, board_id):
    #id에 맞는 게시판 
    board = get_object_or_404(Board, id=board_id)
    # 필터 조건에서 'board' 사용
    posts = Post.objects.filter(board=board)
    return render(request, 'board/post_list.html', {'board': board, 'posts': posts})


def create_post(request, board_id):
    board = get_object_or_404(Board, id=board_id) # 게시판 객체 가져옴

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.board = board  # 폼을 통해 받은 게시글에 게시판 설정
            post.user_id = request.user  # 현재 로그인된 사용자 설정
            post.save()
            return redirect('board/post_detail', board_id=board.id, post_id=post.id) #작성한 게시글 상세 페이지로 리다이렉트
    else:
        form = PostForm()
    return render(request, 'board/post_create.html', {'form': form, 'board': board})

def post_detail(request, board_id, post_id):
    post = get_object_or_404(Post, id=post_id, board_id=board_id)
    return render(request, 'board/post_detail.html', {'post': post})