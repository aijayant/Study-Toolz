from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_user(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Register Succcessfully..')
            return redirect('/AuthApp-/login/')
        else:
            messages.info(request,'Invalid Credentials..')
            return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})

def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username ,password=password)
        if user is not None:
            login(request,user)
            messages.info(request, f'Hello {username},')
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or password ...!!!')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.info(request,'Logged out successfully..')
    return redirect('/')