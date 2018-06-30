"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as main_views
import guestbook.views as guestbook_views
import user.views as user_views

urlpatterns = [ #url에서 post 방식으로 보내는 것들은 마지막에url 부이면안댄다
    path('',main_views.index),
    #user 부분패턴
    path('user/joinform/',user_views.joinform), #회원가입 페이지
    path('user/joinsuccess/', user_views.joinsuccess),  # 회원가입 성공페이지
    path('user/join', user_views.join),  # 회원가입 성공페이지
    path('user/loginform/',user_views.loginform),
    path('user/login',user_views.login),
    path('user/logout', user_views.logout),
    #관리자 부분 패턴
    path('admin/', admin.site.urls), #상대경로는 맨앞에 /가 없읍니다. #관리자페이지

    #guestbook부분 패턴
    path('guestbook/',guestbook_views.guestbook), #방명록 페이지
    path('guestbook/add',guestbook_views.add), # 방명록 추가
    #path('guestbook/',guestbook_views.deleteform_return),
    path('guestbook/deleteform',guestbook_views.deleteformPage), #list에서 deleteform주소로 갔을때 deleteformPage함수실행
    path('guestbook/delete',guestbook_views.delete) # guet

]


