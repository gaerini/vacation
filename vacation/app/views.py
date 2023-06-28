from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Timetable, Like, Timeblock

# Create your views here.

def timetable(request, timetable_pk):

    timetable = Timetable.objects.get(pk=timetable_pk)
    timeblocks = Timeblock.objects.get(timetable_id = timetable_pk)
    return render(request, "timetable.html", {'timetable': timetable, 'timeblocks': timeblocks})

def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('timetable', user.pk)
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
        new_timetable = Timetable.objects.create(
            author = new_user,
        )
        auth.login(request, new_user)

        return redirect('timetable', new_timetable.pk)
    return render(request, 'signup.html')