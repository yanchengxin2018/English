from django.db import models
from django.contrib.auth import get_user_model
UserModel=get_user_model()


#单词表
class EnglishWordModel(models.Model):
    index = models.IntegerField()
    english=models.CharField(max_length=100,help_text='英语单词')
    chinese=models.CharField(max_length=100,help_text='汉语')
    pronunciation=models.CharField(max_length=100,help_text='音标')
    def __str__(self):
        return '{}|{}'.format(self.english,self.chinese)

#记忆加强表
class StrengthenMemoryModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,help_text='记录添加时间')
    user_obj=models.ForeignKey(UserModel,on_delete=models.CASCADE,help_text='用户对象')
    english_obj=models.ForeignKey('EnglishWordModel',on_delete=models.CASCADE,help_text='英语单词对象')
    previous_memory_time=models.DateTimeField(help_text='上次记忆时间')
    next_memory_time=models.DateTimeField(help_text='下次记忆时间')
    memory_power=models.IntegerField(default=1,help_text='记忆力持久度')


#用户记忆记录
class EnglishWordRecordModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,help_text='记录添加时间')
    user_obj=models.ForeignKey(UserModel,on_delete=models.CASCADE,help_text='用户对象')
    english_obj=models.ForeignKey('EnglishWordModel',on_delete=models.CASCADE,help_text='英语单词对象')
    previous_memory_time=models.DateTimeField(help_text='上次记忆时间')
    next_memory_time=models.DateTimeField(help_text='下次记忆时间')
    memory_power = models.IntegerField(default=1,help_text='记忆力持久度')

    def __str__(self):
        return '{}|{}'.format(self.created_at,self.english_obj)






