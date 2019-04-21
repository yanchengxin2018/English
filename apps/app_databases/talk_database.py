from django.db import models
from django.contrib.auth import get_user_model
UserModel=get_user_model()


#谈话
class TalkModel(models.Model):
    user_obj=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    commit_time=models.DateTimeField(auto_now_add=True)
    context=models.CharField(max_length=40)
    class Meta:
        verbose_name_plural='交谈区'
    def __str__(self):
        return '{}-->{}-->{}'.format(self.user_obj.username,self.commit_time,self.context)

