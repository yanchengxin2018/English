# Generated by Django 2.2 on 2019-04-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='pet_name',
        ),
    ]