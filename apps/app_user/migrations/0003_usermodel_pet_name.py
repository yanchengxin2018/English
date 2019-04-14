# Generated by Django 2.2 on 2019-04-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_remove_usermodel_pet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='pet_name',
            field=models.CharField(default=1, help_text='昵称', max_length=20),
            preserve_default=False,
        ),
    ]