from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.forms import model_to_dict
from board.models import Board
# Create your views here.

def writeform(requset):
    #인증 확인
    if requset.sessionp['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')

def boardList(request):
    boardLists = Board.objects.all().order_by('-regdate')
    context = {'boardLists':boardLists}
    return render(request,'board/list.html',context)


def boardWrite(request):
    print(request.session['authuser'])
    return render(request,'board/write.html')

def boardWrite_Save(request):
        # 리스트에 담아버림, 없으면 오류

    writeSave = Board()
    writeSave.user_id = request.session['authuser']['id'] # session 에서 authuser딕셔너리의 id 값을 받아옴
    writeSave.name = request.session['authuser']['name']
    writeSave.title = request.POST['title']
    writeSave.content = request.POST['content']
    writeSave.save()

    return HttpResponseRedirect('/board')


def boardView(request):
    pk = request.GET['id'] # 아디를 받음여
    boardData = Board.objects.get(id=pk) #id값과 같은 객체데이타를 부름
    Board.objects.filter(id=pk).update(hit=boardData.hit + 1)#아이디와 같은 값

    boardViews = Board.objects.get(id=request.GET.get('id'))
    context = {'boardViews':boardViews}
    return render(request,'board/view.html',context)




def boardModify(request):

    boardModify = Board.objects.get(id=request.GET.get('id'))
    context = {'boardModify':boardModify}
    return render(request,'board/modify.html',context)

def Modify_Save(request):

    Modify_Saves_id = request.POST.get('id')
    Modify_Save=Board.objects.get(id=Modify_Saves_id)
    Modify_Save.title = request.POST['title']
    Modify_Save.content = request.POST['content']
    Modify_Save.save()

    return HttpResponseRedirect('/board/view?id='+Modify_Saves_id)


def list_Delete(request):

    list_Delete= request.GET.get('id')
    Board.objects.filter(id=list_Delete).delete()

    return HttpResponseRedirect('/board')

def list_Find(request):
    #print(request.POST)
    list_find= request.POST.get('find')
    print("dasdf",list_find)
    if list_find:
        list_finds = Board.objects.filter(name=list_find)
        context={'list_finds',list_finds}
        print(context)
