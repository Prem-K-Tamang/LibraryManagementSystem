from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.hashers import make_password


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:       
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.success(request,('Invalid username or password! '))
                return redirect('admin_login')
        else:
            if request.user.is_authenticated:
                return redirect('dashboard')
            return render(request, 'auth/login.html')


def change_admin_pw(request):
    if request.method == 'POST':
        name = request.user.username
        user = get_object_or_404(User,username=name)
        form = UserForm(request.POST or None)
        if form.is_valid():
            user.password=make_password(form.cleaned_data['password'])
            user.save() 
            messages.success(request, 'Password has been updated!')
            return redirect('admin_login')   
        else:
            messages(request, 'Failed to change password!')
            return redirect('change_admin_pw')

        return redirect('dashboard')
    elif request.method == 'GET':
        return render(request, 'auth/change_password.html')


def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


