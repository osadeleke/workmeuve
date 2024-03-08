from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Bus, Driver, Ticket, User


@login_required(login_url='loginPage')
def index(request):
    buses = Bus.objects.all()
    return render(request, 'workmeuve/home.html', {'buses': buses})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'workmeuve/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Logged out..')
    return redirect('loginPage')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + 'Account created successfully')
                return redirect('loginPage')
        return render(request, 'workmeuve/registration.html', context)
    
def bus(request, plate_no):
    bus = Bus.objects.get(plate_no=plate_no)
    return render(request, 'workmeuve/bus.html', {'bus': bus})