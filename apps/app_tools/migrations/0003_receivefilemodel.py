# Generated by Django 2.2 on 2019-04-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_tools', '0002_delete_receivefilemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiveFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='static/files')),
            ],
        ),
    ]
