# Generated by Django 2.2 on 2019-04-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_databases', '0012_talkmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talkmodel',
            options={'verbose_name_plural': '交谈区'},
        ),
        migrations.AlterField(
            model_name='talkmodel',
            name='context',
            field=models.CharField(max_length=40),
        ),
    ]