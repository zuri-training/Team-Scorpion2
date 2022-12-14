from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class UploadedFiles(models.Model):
    files_Upload = models.FileField(upload_to='media', blank=False)
    filename = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.filename

