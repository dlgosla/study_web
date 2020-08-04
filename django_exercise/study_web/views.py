from django.shortcuts import render

def index(request):
    return render(request, 'study_web/index.html', {})

def login(request):
    return render(request, 'study_web/login.html', {})