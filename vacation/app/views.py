from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Timetable, Like, Timeblock, Tablelist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def timetable(request, timetable_pk):

    timetable = Timetable.objects.get(pk=timetable_pk)
    timeblocks = Timeblock.objects.filter(timetable_id = timetable_pk)
    return render(request, "timetable.html", {'timetable': timetable, 'timeblocks': timeblocks})

def tablelist(request, timetable_pk):
    
    timetable = Timetable.objects.get(pk=timetable_pk)
    tablelists = Tablelist.objects.filter(timetable_id = timetable)

    return render(request, "tablelist.html", {'tablelists' : tablelists})

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

@csrf_exempt
def timeblock(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        timetable_pk = int(request_body['timetable_pk'])
        timeblock_start = int(request_body['timeblock_start'])
        timeblock_end = int(request_body['timeblock_end'])
        detail = request_body['timeblock_detail']

        timetable = Timetable.objects.get(pk=timetable_pk)

        timeblock = Timeblock.objects.create(
                timetable_id = timetable,
                starttime = timeblock_start,
                endtime = timeblock_end,
                detail = detail,
        )


        timeblocks = Timeblock.objects.filter(timetable_id=timetable_pk)
        shit = 0
        response = {
            
        }
        return HttpResponse(json.dumps(list(response)))