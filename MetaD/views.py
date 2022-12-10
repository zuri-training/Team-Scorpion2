from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserInfoForm

# to restrict unauthorized users from certain page, use:
from django.contrib.auth.decorators import login_required 

'''the put @Login_required on the page section...
then specify in settings: redirect in settings...'''


# Create your views here.

def landingPage(request):
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'about.html')


def signup_page(request):

    trim = UserInfoForm
    slight_trim = {'Lean_Trim': trim}

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        other_user = User.objects.create_user(username, email, password)
        other_user.first_name = first_name
        other_user.last_name = last_name

        other_user.save()
        return HttpResponseRedirect(reverse('log-page'))

    return render(request, 'signup.html', context=slight_trim)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect in real case will be to the pages authenticated users have access to, not home-page
            return HttpResponseRedirect(reverse('first-page'))
        else:
            return HttpResponse('User does not exist')
        # return redirect('sign-page')
         
    return render(request, 'login.html', {})
