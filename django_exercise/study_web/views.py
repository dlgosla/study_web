from django.shortcuts import render
from django.http import HttpResponse
from .models import DjangoBoard

def index(request):
    boardList = DjangoBoard.objects.all() #모든 object를 불러와서 boardList에 저장
    context = {'boardList':boardList} #context에 boardList안에 정보들을 저장
    return render(request, 'study_web/index.html', context) #study_web/index.html에 context의 정보를 전달

def login(request):
    return render(request, 'study_web/login.html', {})
