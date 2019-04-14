# Generated by Django 2.2 on 2019-04-14 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_databases', '0003_englishwordmodel_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishWordRecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='记录添加时间')),
                ('previous_memory_time', models.DateTimeField(help_text='上次记忆时间')),
                ('next_memory_time', models.DateTimeField(help_text='下次记忆时间')),
                ('english_obj', models.ForeignKey(help_text='英语单词对象', on_delete=django.db.models.deletion.CASCADE, to='app_databases.EnglishWordModel')),
                ('user_obj', models.ForeignKey(help_text='用户对象', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]