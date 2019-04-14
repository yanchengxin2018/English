from rest_framework import serializers
from app_databases.models import StrengthenMemoryModel,EnglishWordRecordModel,EnglishWordModel


#从记忆加强数据库得到单词
class StrengthenCardSerializer(serializers.ModelSerializer):

    card_type = serializers.SerializerMethodField()
    index = serializers.CharField(source='english_obj.index')
    english = serializers.CharField(source='english_obj.english')
    chinese = serializers.CharField(source='english_obj.chinese')
    pronunciation = serializers.CharField(source='english_obj.pronunciation')
    previous_memory_time = serializers.SerializerMethodField()

    def get_card_type(self,strengthen_obj):
        return 'strengthen'

    def get_previous_memory_time(self,strengthen_obj):
        return '上次记忆时间'

    class Meta:
        model=StrengthenMemoryModel
        fields=('index','english','chinese','pronunciation',
                'card_type','previous_memory_time',)


#从记忆历史数据库得到单词
class EnglishWordRecordCardSerialzer(serializers.ModelSerializer):
    card_type = serializers.SerializerMethodField()
    index = serializers.CharField(source='english_obj.index')
    english = serializers.CharField(source='english_obj.english')
    chinese = serializers.CharField(source='english_obj.chinese')
    pronunciation = serializers.CharField(source='english_obj.pronunciation')
    previous_memory_time = serializers.SerializerMethodField()

    def get_card_type(self, strengthen_obj):
        return 'record'

    def get_previous_memory_time(self, strengthen_obj):
        return '上次记忆时间'

    class Meta:
        model = EnglishWordRecordModel
        fields = ('index', 'english', 'chinese', 'pronunciation',
                  'card_type', 'previous_memory_time',)


#从全部单词数据库得到单词
class EnglishWordSerializer(serializers.ModelSerializer):

    card_type=serializers.SerializerMethodField()

    def get_card_type(self, strengthen_obj):
        return 'new_card'

    class Meta:
        model=EnglishWordModel
        fields = ('index', 'english', 'chinese', 'pronunciation',
                  'card_type',)


#新建一条记忆记录
class EnglishWordRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model=EnglishWordRecordModel
        fields=('user_obj','english_obj','previous_memory_time','next_memory_time','memory_power',)


#新建一条记忆记录试图的序列化器
class EnglishWordRecordViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model=EnglishWordModel
        fields=('index',)


#信息卡
class InfoCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=EnglishWordRecordModel
        fields=('',)


