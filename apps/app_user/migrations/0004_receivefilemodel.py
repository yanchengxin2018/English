# Generated by Django 2.2 on 2019-04-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_usermodel_pet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiveFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]