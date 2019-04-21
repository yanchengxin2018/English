from rest_framework import serializers
from app_databases.models import EnglishWordModel, LevelModel
from app_tools.models import ReceiveFileModel
from django.conf import settings


# 制作单词数据库
class MakeEnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWordModel
        fields = ('id', 'index', 'english', 'chinese', 'pronunciation',)

    def create(self, validated_data):
        index = validated_data.get('index')
        english_word_obj = EnglishWordModel.objects.filter(pk=index).first()
        if english_word_obj:
            serializer_update_obj = MakeEnglishWordSerializer(english_word_obj, validated_data)
            serializer_update_obj.is_valid(raise_exception=True)
            return serializer_update_obj.save()
        else:
            return super().create(validated_data)


# 英语单词列表
class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWordModel
        fields = ('id', 'index', 'english', 'chinese', 'pronunciation',)


# 记忆强度等级初始化
class LevelSerializer(serializers.ModelSerializer):
    choices = (
        (1, '开始初始化'),
        (2, '开始更新'),
    )
    order = serializers.ChoiceField(choices=choices, write_only=True)

    class Meta:
        model = LevelModel
        fields = ('level', 'time_long', 'cycle', 'order',)
        read_only_fields = ('level', 'time_long', 'cycle',)


# 接收文件
class ReceiveFileSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    file = serializers.FileField(use_url=False, help_text='选择一个文件')

    def get_path(self, obj):
        ip = settings.IP
        path = 'http://{}/{}'.format(ip, obj.file)
        return path

    class Meta:
        model = ReceiveFileModel
        fields = ('id', 'file', 'path',)


#更换ip
class IP2IPSerializer(serializers.Serializer):
    ip_1=serializers.CharField(help_text='要修改的字符串是什么？')
    ip_2=serializers.CharField(help_text='要把这个字符串修改为什么？')
    user_setting_ip=serializers.BooleanField(default=False,help_text='点选此处,意味着将把这个字符串修改为配置里的IP')











