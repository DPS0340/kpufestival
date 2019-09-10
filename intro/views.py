from django.shortcuts import render, get_object_or_404, redirect
from .models import Intro

# introduce 기능
# introduce-학과명,좋아요개수,위치,소개글 표시/모달에서 지도 표시
# intro_detail
# -학과명,좋아요 개수,싫어요 개수,조회수,태그,소개글,학과 아이콘 표시/모달에서 지도 표시
# -카톡 공유하기 기능(학과명,사진 공유 혹은 링크)#

def introduce(request):
    all_intro=Intro.objects.all()

    return render(request,'introduce.html', { 'all_intro':all_intro })

def intro_detail(request, intro_id):
    intro_detail = get_object_or_404(Intro, pk=intro_id)
    return render(request,'intro_detail.html', {'intro_detail': intro_detail})


def intro_like(request, intro_id):
    intro = get_object_or_404(Intro, id=intro_id)
    if request.user in intro.intro_like_users.all():
        intro.intro_like_users.remove(request.user)
    else:
        intro.intro_like_users.add(request.user)
    return redirect('/intro/intro_detail/' + str(intro.id))
