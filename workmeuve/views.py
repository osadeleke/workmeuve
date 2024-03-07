from django.shortcuts import render


def index(request):
    return render(request, 'workmeuve/index.html')

def login(request):
    return render(request, 'workmeuve/login.html')

def register(request):
    return render(request, 'workmeuve/registration.html')