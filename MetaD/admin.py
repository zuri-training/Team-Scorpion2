from django.contrib import admin
from .models import UserInfo, UploadedFiles
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(UploadedFiles)
