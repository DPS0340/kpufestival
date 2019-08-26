from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth
# 파일 저장 import문
from django.core.files.storage import FileSystemStorage

from .models import Board, Comment
from .forms import BoardPost, PostSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q

# 메세지 라이브러리
from django.contrib import messages

from django.conf import settings
from django.shortcuts import render

# 게시판 카테고리 별 순서
from django.db.models import Count

from django.db.models import Max 

def board(request):
    boards=Board.objects
    # 댓글 수
    counts=Board.objects.count()

    board_list=Board.objects.all()
        
    #페이지
    paginator = Paginator(board_list,5)
    total_len=len(board_list)

    page = request.GET.get('page',1)
    posts = paginator.get_page(page)
    
    try:
        lines = paginator.page(page) 
    except PageNotAnInteger: 
        lines = paginator.page(1) 
    except EmptyPage: 
        lines = paginator.page(paginator.num_pages) 
        
    index = lines.number -1 
    max_index = len(paginator.page_range) 
    start_index = index -2 if index >= 2 else 0 
    if index < 2 : 
        end_index = 5-start_index
    else : 
        end_index = index+3 if index <= max_index - 3 else max_index 
    page_range = list(paginator.page_range[start_index:end_index]) 
    
    context = { 'boards':boards,'board_list': lines ,'counts':counts, 'posts':posts, 'page_range':page_range, 'total_len':total_len, 'max_index':max_index-2 } 
    return render (request,'board.html', context )


def board_detail(request, board_id):
    details = get_object_or_404(Board, pk=board_id)
    return render(request, 'board_detail.html', {'details': details})

def new(request):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            post.author=request.user
            # 날짜는 자동으로 현재 입력해주는 것
            post.pub_date = timezone.now()
            post.save()
            return redirect('board')     # 바로 home으로 redirect
        
        else: #아무것도 안쓰고 글쓰기 눌렀을 때
            messages.info(request, '내용을 입력하세요!')
            return redirect('new')
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = BoardPost()
        return render(request, 'board_new.html', {'form':form}) # form형태로 전달

def introduce(request):
    return render(request,'introduce.html')

def intro_detail(request):
    return render(request,'intro_detail.html')
