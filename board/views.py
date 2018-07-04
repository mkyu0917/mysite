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
    #k=request.session['authuser']
    writeSave.user_id = request.session['authuser']['id'] # session 에서 authuser딕셔너리의 id 값을 받아옴
    writeSave.name = request.session['authuser']['name']
    writeSave.title = request.POST['title']
    writeSave.content = request.POST['content']


    writeSave.save()

    return HttpResponseRedirect('/board')


def boardView(request):

    boardViews = Board.objects.filter(id=request.GET.get('id')).get()
   # print(boardViews)

    context = {'boardViews':boardViews}

    return render(request,'board/view.html',context)

def boardModify(request):
    boardModify = Board.objects.filter(id=request.GET.get('id')).get()
    context = {'boardModify':boardModify}
    print(context)
    return render(request,'board/modify.html',context)

def Modify_Save(request): #id값을 받아와야지
        #print(request.POST)

        Modify_Saves_id = request.POST['id']
        Modify_Save=Board.objects.filter(id=Modify_Saves_id)
        Modify_Save.title = request.POST['title']
        Modify_Save.content = request.POST['content']

        Modify_Save.update()
        # Modify_Save.id = request.POST['id']
        # # Board.objects.filter(id=Modify_Saves_id).filter(title=Modify_Saves_title).filter(content=Modify_Saves_content).update()

        return HttpResponseRedirect('/board')




    #boardModify_Save = request.POST.get('id')
    #print(boardModify_Save)
    #print('asefawegaweafef',boardModify_Save)

    #print('asljefoasiejf',boardModify_Save['id'])
    # if  request.GET.get('user_id') == request.session['authuser']['id']:
    #
    #     boardModify_Save.title = request.GET.get('title')
    #     boardModify_Save.content = request.GET.get('content')
    #     boardModify_Save.save()
    # return HttpResponseRedirect('/board/view')

