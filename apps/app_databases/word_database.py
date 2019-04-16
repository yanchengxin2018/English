from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# 单词表
class EnglishWordModel(models.Model):
    index = models.IntegerField()
    english = models.CharField(max_length=100, help_text='英语单词')
    chinese = models.CharField(max_length=100, help_text='汉语')
    pronunciation = models.CharField(max_length=100, help_text='音标')

    def __str__(self):
        return '{}|{}'.format(self.english, self.chinese)


# 记忆加强表
class StrengthenMemoryModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text='记录添加时间')
    user_obj = models.ForeignKey(UserModel, on_delete=models.CASCADE, help_text='用户对象')
    english_obj = models.ForeignKey('EnglishWordModel', on_delete=models.CASCADE, help_text='英语单词对象')
    level = models.IntegerField(default=0, help_text='单词级别')
    next_memory_time = models.DateTimeField(help_text='下次记忆时间')

    # previous_memory_time=models.DateTimeField(help_text='上次记忆时间')
    # memory_power=models.IntegerField(default=1,help_text='记忆力持久度')
    class Meta:
        verbose_name_plural = '记忆加强数据库'


# 用户记忆记录
class EnglishWordRecordModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text='记录添加时间')
    user_obj = models.ForeignKey(UserModel, on_delete=models.CASCADE, help_text='用户对象')
    english_obj = models.ForeignKey('EnglishWordModel', on_delete=models.CASCADE, help_text='英语单词对象')
    level = models.IntegerField(default=0, help_text='单词级别')
    next_memory_time = models.DateTimeField(help_text='下次记忆时间')

    def __str__(self):
        return '{}|{}'.format(self.created_at, self.english_obj)

    class Meta:
        verbose_name_plural = '记忆记录数据库'

'''

有一个数据表XxxModel,有下面3个字段
创建时间字段cread_at/整数字段int_xxx/另外一个时间字段next_time

1.拥有相同int_xxx的数据属于同一组,每组仅保留一条,这条的cread_at是同组中最大(晚)的
2.每组保留了一条数据以后组成新的集合
3.取集合中next_time最小(早)的

'''







