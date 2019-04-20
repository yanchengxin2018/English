from rest_framework import serializers
from app_databases.models import StrengthenMemoryModel, EnglishWordRecordModel, EnglishWordModel
from django.conf import settings
import os, random


# 制作一张加强卡
class StrengthenCardSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='strengthen', read_only=True)
    word_index = serializers.CharField(source='english_obj.index')
    chinese = serializers.CharField(source='english_obj.chinese')
    update_image = serializers.SerializerMethodField()

    def get_update_image(self, obj):
        base_dir = settings.BASE_DIR
        ip = settings.IP
        back_dir = '{}/static/HTML/start/update_backs'.format(base_dir)
        files = os.listdir(back_dir)
        try:
            rand = random.randint(0, len(files) - 1)
            img = files[rand]
        except:
            img = ''
        img_path = '{}/static/HTML/start/update_backs/{}'.format(ip, img)
        return img_path

    class Meta:
        model = StrengthenMemoryModel
        fields = ('word_index', 'chinese', 'card_type','update_image',)


# 制作一张升级卡
class UpdateCardSerializer(serializers.ModelSerializer):
    word_index = serializers.CharField(source='english_obj.index')
    chinese = serializers.CharField(source='english_obj.chinese')
    card_type = serializers.CharField(default='update_card', read_only=True)
    update_image=serializers.SerializerMethodField(read_only=True)

    def get_update_image(self,obj):
        base_dir = settings.BASE_DIR
        ip = settings.IP
        back_dir = '{}/static/HTML/start/update_backs'.format(base_dir)
        files = os.listdir(back_dir)
        try:
            rand = random.randint(0, len(files) - 1)
            img = files[rand]
        except:
            img = ''
        img_path = '{}/static/HTML/start/update_backs/{}'.format(ip, img)
        return img_path

    class Meta:
        model = EnglishWordRecordModel
        fields = ('word_index', 'chinese', 'card_type','update_image',)


# 从全部单词数据库得到单词
class EnglishWordSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='new_card')
    word_index=serializers.CharField(source='index')
    back_image=serializers.SerializerMethodField()

    def get_back_image(self,obj):
        base_dir=settings.BASE_DIR
        ip=settings.IP
        back_dir='{}/static/HTML/start/new_backs'.format(base_dir)
        files=os.listdir(back_dir)
        try:
            rand=random.randint(0,len(files)-1)
            img = files[rand]
        except:
            img=''
        img_path='{}/static/HTML/start/new_backs/{}'.format(ip,img)
        return img_path

    class Meta:
        model = EnglishWordModel
        fields = ('word_index', 'english', 'chinese', 'pronunciation', 'card_type','back_image',)


# 加入普通记录
class EnglishWordRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWordRecordModel
        fields = ('user_obj', 'english_obj', 'previous_memory_time', 'next_memory_time', 'memory_power',)


# 提交一张记忆卡片
class MemoryCardCommitSerializer(serializers.ModelSerializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index',)


# 提交一张加强卡片
class StrengthenCardCommitSerializer(serializers.ModelSerializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')
    spell = serializers.CharField(help_text='拼写的内容')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index', 'spell',)


# 提交一张升级卡片
class UpdateCardCommitSerializer(serializers.ModelSerializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')
    spell = serializers.CharField(help_text='拼写的内容')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index', 'spell',)
