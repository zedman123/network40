from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == '':
            messages.info(request, 'please enter a password')
        elif password2 == '':
            messages.info(request, 'you did not confirm the password')
        elif username == '':
            messages.info(request, 'you did not enter a username')
        elif password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
        return redirect('register')

    else:
        return render(request, 'login1.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You have successsfuly logged in')
            return redirect('welcome')

        else:
            messages.info(request, 'invalid credantials')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def welcome(request):
    return render(request, 'welcome.html')
