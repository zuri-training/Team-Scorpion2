from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserInfoForm,UploadedFilesForm
from MetaD.models import UploadedFiles
from django.contrib import messages
# from keyboard import press
import subprocess
 
import os

# to restrict unauthorized users from certain page, use:
from django.contrib.auth.decorators import login_required 

'''the put @Login_required on the page section...
then specify in settings: redirect in settings...'''


# Create your views here.

def landingPage(request):
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup_page(request):

    trim = UserInfoForm
    slight_trim = {'Lean_Trim': trim}

    if request.method == 'POST':
        mitigate = trim(request.POST)
    
        if mitigate.is_valid():
            user = mitigate.save()
            user.set_password(user.password)
        


            mitigate.save()
            
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
            messages.info(request,'Wrong username or password')
         
    return render(request, 'login.html', {})

@login_required
def log_out_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('first-page'))


@login_required
def dashboard(request):
    form = UploadedFilesForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UploadedFilesForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            file = request.FILES.get('files_Upload')
            """
                you don't actually need a file name field though
                you can get the name of the file by doing field.name
            """
            new_file = UploadedFiles.objects.create(
                files_Upload = file,
                filename = file.name
            )

            # servers = inputfile.save()
            # input_file = f"/Team-Scorpion2/media/{servers}"

            exe = "Scripts/exiftool(-k).exe"
            # exe = "hachoir-metadata"

            # print(exe)
            # C:\Users\User\Desktop\brain\New folder (2)\Team-Scorpion2-change\Scripts\exiftool(-k).exe
            media = new_file.files_Upload.url.lstrip('/')
            process = subprocess.Popen([exe, media], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            # press('enter')
            for output in process.stdout:
                print(output.strip())
                
            


    return render(request, 'dashboard.html', context=context)
