from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'main/index.html')

def guestboard(request):
    return render(request,'guestbook/list.html')
