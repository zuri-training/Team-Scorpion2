from django import forms
from django.contrib.auth.models import User
from .models import UserInfo, UploadedFiles


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        field = (all)


class UploadedFilesForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        field = (all)