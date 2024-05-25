
from .models import Password
from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from .forms import UserRegisterForm

def signupPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('menu')  
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('menu')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('menu')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutPage(request):

        auth_logout(request)
        return redirect('login') 

def menu(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == "POST":
        username = request.POST.get('username', '')  
        url = request.POST.get('url', '')  
        password = request.POST.get('pwd', '')  
        
       
        if username:
            Password.objects.create(url=url, username=username, password=password)
            return redirect('menu')  
        else:
           
            pass
        
    entries = Password.objects.all()
    return render(request, 'password.html', {'entries': entries})

def notes(request):
    return render(request, 'notes.html')
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')
