# Generated by Django 2.2 on 2019-04-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishWordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('english', models.CharField(help_text='英语单词', max_length=100)),
                ('chinese', models.CharField(help_text='汉语', max_length=100)),
                ('pronunciation', models.CharField(help_text='音标', max_length=100)),
            ],
        ),
    ]