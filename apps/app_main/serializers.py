import datetime
from rest_framework import serializers
from app_databases.models import StrengthenMemoryModel, EnglishWordRecordModel, EnglishWordModel


# 从记忆加强数据库得到单词
class StrengthenCardSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='strengthen',read_only=True)
    index = serializers.CharField(source='english_obj.index')
    english = serializers.CharField(source='english_obj.english')
    chinese = serializers.CharField(source='english_obj.chinese')
    pronunciation = serializers.CharField(source='english_obj.pronunciation')
    previous_memory_time = serializers.SerializerMethodField()

    def get_previous_memory_time(self, strengthen_obj):
        return str(strengthen_obj)

    class Meta:
        model = StrengthenMemoryModel
        fields = ('index', 'english', 'chinese', 'pronunciation',
                  'card_type', 'previous_memory_time',)


# 从记忆历史数据库得到单词
class EnglishWordRecordCardSerialzer(serializers.ModelSerializer):
    index = serializers.CharField(source='english_obj.index')
    english = serializers.CharField(source='english_obj.english')
    chinese = serializers.CharField(source='english_obj.chinese')
    pronunciation = serializers.CharField(source='english_obj.pronunciation')
    previous_memory_time = serializers.DateTimeField(format='%Y年%m月%d日%H点%M分%S秒')
    card_type = serializers.CharField(default='record', read_only=True)

    class Meta:
        model = EnglishWordRecordModel
        fields = ('index', 'english', 'chinese', 'pronunciation',
                  'card_type', 'previous_memory_time',)


# 制作一张升级卡
class UpdateCardSerializer(serializers.ModelSerializer):
    index = serializers.CharField(source='english_obj.index')
    english = serializers.CharField(source='english_obj.english')
    card_type = serializers.CharField(default='update_card', read_only=True)

    class Meta:
        model = EnglishWordRecordModel
        fields = ('index', 'english', 'card_type',)


# 从全部单词数据库得到单词
class EnglishWordSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(default='new_card')

    class Meta:
        model = EnglishWordModel
        fields = ('index', 'english', 'chinese', 'pronunciation',
                  'card_type',)


# 请求新的卡片
class EnglishWordRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWordRecordModel
        fields = ('user_obj', 'english_obj', 'previous_memory_time', 'next_memory_time', 'memory_power',)


# 提交一张记忆卡片
class MemoryCardCommitSerializer(serializers.Serializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index',)


# 提交一张加强卡片
class StrengthenCardCommitSerializer(serializers.Serializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')
    spell = serializers.CharField(help_text='拼写的内容')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index', 'spell',)


# 提交一张升级卡片
class UpdateCardCommitSerializer(serializers.Serializer):
    word_index = serializers.IntegerField(write_only=True, help_text='单词索引')
    spell = serializers.CharField(help_text='拼写的内容')

    class Meta:
        model = EnglishWordModel
        fields = ('word_index', 'spell',)
