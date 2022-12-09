from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
#to restrict unauthorized users from certain page, use:
from django.contrib.auth.decorators import login_required 

'''the put @Login_required on the page section...
then specify in settings: redirect in settings...'''




# Create your views here.

def landingPage(request):
    return render(request, 'demo/index.html', {})

def signUp(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        u_name = request.POST.get('u_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        other_user = User.objects.create_user(u_name, email, password)
        other_user.first_name = f_name
        other_user.last_name = l_name

        other_user.save()

        return redirect('login-page')

    return render(request, 'demo/signup.html', {})

def logIn(request):
    if request.method == 'POST':
        u_name = request.POST.get('u_name')
        password = request.POST.get('password')

        user = authenticate(request, username = u_name, password = password)
        if user is not None:
            login(request, user)
            # redirect in real case will be to the pages authenticated users have access to, not home-page
            return redirect('home-page')
        else:
            return HttpResponse('User does not exist')
            # return redirect('signup-page')
         
    return render(request, 'demo/login.html', {})