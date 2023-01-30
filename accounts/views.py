from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, message='Sorry. This email address already exists!')
            return redirect(to='accounts:register')
        else:
            user = User(username=username,first_name=first_name, last_name=last_name,
                        email=email, password=password)

            user.save()
            messages.success(request, message='You have been Registered successfully')
            return redirect(to='all:index')

    else:
        return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You have been successfully logged in')
                return redirect(to='all:index')
            else:
                messages.error(request, message='This user is not Active')
                return redirect(to='accounts:login')
        else:
            messages.error(request, 'Invalid Login Details. Please Try again')
            return redirect(to='accounts:login')

    else:
        return render(request, 'accounts/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(to='all:index')
