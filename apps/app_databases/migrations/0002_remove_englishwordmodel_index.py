# Generated by Django 2.2 on 2019-04-13 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_databases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='englishwordmodel',
            name='index',
        ),
    ]
