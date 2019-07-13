from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('hoddme.html')  ##여기 로그인 된 다음페이지 url설정

    return render(request, "signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home') ##여기 로그인 된 다음페이지 url설정
        else:
            return render(request, 'login.html',{'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login.html')
    return render(request, 'login.html')