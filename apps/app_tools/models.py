from django.db import models


# 接收文件
class ReceiveFileModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='static/files')
