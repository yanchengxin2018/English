from rest_framework import serializers
from app_databases.models import StrengthenMemoryModel, EnglishWordRecordModel, EnglishWordModel


# 制作一张加强卡
class StrengthenCardSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='strengthen', read_only=True)
    index = serializers.CharField(source='english_obj.index')
    chinese = serializers.CharField(source='english_obj.chinese')

    class Meta:
        model = StrengthenMemoryModel
        fields = ('index', 'chinese', 'card_type',)


# 制作一张升级卡
class UpdateCardSerializer(serializers.ModelSerializer):
    index = serializers.CharField(source='english_obj.index')
    chinese = serializers.CharField(source='english_obj.chinese')
    card_type = serializers.CharField(default='update_card', read_only=True)

    class Meta:
        model = EnglishWordRecordModel
        fields = ('index', 'chinese', 'card_type',)


# 从全部单词数据库得到单词
class EnglishWordSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='new_card')

    class Meta:
        model = EnglishWordModel
        fields = ('index', 'english', 'chinese', 'pronunciation', 'card_type',)


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
