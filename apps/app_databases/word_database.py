from django.db import models


#单词表
class EnglishWordModel(models.Model):
    index = models.IntegerField()
    english=models.CharField(max_length=100,help_text='英语单词')
    chinese=models.CharField(max_length=100,help_text='汉语')
    pronunciation=models.CharField(max_length=100,help_text='音标')











