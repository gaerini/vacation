from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Timetable, Like

# Create your views here.
def home(request):
    #logic here
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, 'login.html', {"error":error})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']

        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'signup.html', {"error":error})
        
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)

        return redirect('home')
    return render(request, 'signup.html')