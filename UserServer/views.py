from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from UserServer.models import UserAccount as LogDao
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import UserAccount


# http://localhost/appname/xxx
# def login(request):
#     return HttpResponse("登录成功!!")


# 要做接受的报文和返回数据
# 登录模块
# 到mysql中验证，验证成功则提示验证成功.否则提示用户不存在
# Django不接受回应报文的方法头，所以要单独列出一url漫游来集体区分其中的方法
# coding=utf-8


# Create your views here.
class UserForm(forms.Form):
    UserId = forms.CharField(label='用户名', max_length=50)
    UserPassword = forms.CharField(label='密码', widget=forms.PasswordInput())
    IsAdmin = forms.CharField(label='是否为系统管理员')
    SurePassword = forms.CharField(label='确认密码', widget=forms.PasswordInput())


def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            UserId = userform.cleaned_data['UserId']
            UserPassword = userform.cleaned_data['UserPassword']
            SurePassword = userform.cleaned_data['SurePassword']
            if UserAccount.objects.exists(UserId=UserId):
                return render(request, 'register.html', {'Error': '已存在该用户'})
            elif UserPassword == SurePassword and UserPassword != '' and len(UserPassword) >= 8:
                admin = 'NO'
                UserAccount.objects.create(UserId=UserId, UserPassword=UserPassword, IsAdmin=admin)
                UserAccount.save()
                return render(request, 'register.html', {'OK': '注册成功'})
    else:
        userform = UserForm()
    return render(request, 'register.html', {'userform': userform})


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            UserId = userform.cleaned_data['UserId']
            UserPassword = userform.cleaned_data['UserPassword']
            IsAdmin = userform.cleaned_data['IsAdmin']
            user = UserAccount.objects.filter(UserId=userform.cleaned_data['UserId'],
                                              UserPassword=userform.cleaned_data['UserPassword'],
                                              IsAdmin=userform.cleaned_data['IsAdmin'])
        if userform.cleaned_data['IsAdmin'] == 'NO' and UserAccount.objects.filter(
                UserId=userform.cleaned_data['UserId'], UserPassword=userform.cleaned_data['UserPassword'],
                IsAdmin=userform.cleaned_data['IsAdmin']):
            return index(request)
        else:
            return render(request, 'login.html', {'userform': '用户名或密码错误，请重新输入'})
    else:
        userform = UserForm()
    return render(request, 'login.html', {'userform': userform})


def loginA(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            UserId = userform.cleaned_data['UserId']
            UserPassword = userform.cleaned_data['UserPassword']
            IsAdmin = userform.cleaned_data['IsAdmin']
            user = UserAccount.objects.filter(UserId=userform.cleaned_data['UserId'],
                                              UserPassword=userform.cleaned_data['UserPassword'],
                                              IsAdmin=userform.cleaned_data['IsAdmin'])
        if UserAccount.objects.filter(
                UserId=userform.cleaned_data['UserId'], UserPassword=userform.cleaned_data['UserPassword'],
                IsAdmin='YES'):
            return indexRoot(request)
        else:
            return render(request, 'login_two.html', {'userform': '用户名或密码错误，请重新输入'})
    else:
        userform = UserForm()
    return render(request, 'login_two.html', {'userform': userform})


def commencement(request):
    return render(request, 'commencement.html')


def index(request):
    return HttpResponseRedirect('map/')


def indexRoot(request):
    return render(request, 'maproot/')
