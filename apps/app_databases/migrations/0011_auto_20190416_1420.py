# Generated by Django 2.2 on 2019-04-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_databases', '0010_auto_20190416_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strengthenmemorymodel',
            name='memory_power',
        ),
        migrations.RemoveField(
            model_name='strengthenmemorymodel',
            name='previous_memory_time',
        ),
        migrations.AddField(
            model_name='strengthenmemorymodel',
            name='level',
            field=models.IntegerField(default=0, help_text='单词级别'),
        ),
    ]