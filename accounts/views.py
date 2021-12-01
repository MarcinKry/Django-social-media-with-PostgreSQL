from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['emailname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create_user(firstname = firstname, lastname=lastname, username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created succesfully')
        return redirect('login')
    return render(request, 'accounts/register.html')