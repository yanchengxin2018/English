# Generated by Django 2.2 on 2019-04-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_databases', '0006_auto_20190414_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(help_text='记忆等级')),
                ('time_long', models.DateTimeField(help_text='时间长度')),
                ('cycle', models.CharField(choices=[('d', '短期记忆'), ('z', '中期记忆'), ('c', '长期记忆')], help_text='记忆周期', max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='englishwordrecordmodel',
            options={'verbose_name_plural': '记忆记录数据库'},
        ),
        migrations.AlterModelOptions(
            name='strengthenmemorymodel',
            options={'verbose_name_plural': '记忆加强数据库'},
        ),
    ]