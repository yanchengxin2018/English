from django.db import models


#记忆强度等级
class LevelModel(models.Model):
    choices=(
        ('d','短期记忆'),
        ('z','中期记忆'),
        ('c','长期记忆'),
    )
    level=models.IntegerField(help_text='记忆等级',unique=True)
    time_long=models.IntegerField(help_text='时间长度')
    cycle=models.CharField(choices=choices,help_text='记忆周期',max_length=10)


