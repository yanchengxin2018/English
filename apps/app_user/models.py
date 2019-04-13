from django.contrib.auth.models import AbstractUser
from django.db import models


#用户表
class UserModel(AbstractUser):
    pet_name=models.CharField(max_length=20,help_text='昵称')


#接收文件
class ReceiveFileModel(models.Model):
    file=models.FileField()







