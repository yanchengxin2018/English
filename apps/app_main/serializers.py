from rest_framework import serializers
from app_databases.models import StrengthenMemoryModel,EnglishWordRecordModel,EnglishWordModel
from app_exception import custom_exceptions
import datetime


from app_tools.app_tools_serializer import get_view_from_serializer

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


#EnglishWordRecordViewSet视图post字段序列化器
class EnglishWordRecordViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model=EnglishWordModel
        fields=('index',)


#TestCardCommitViewSet视图post字段序列化器
class TestCardCommitViewSetSerializer(serializers.Serializer):
    index=serializers.CharField()
    word_input=serializers.CharField()
    card_type=serializers.CharField()


#信息卡
class InfoCardSerializer(serializers.ModelSerializer):
    # 记忆类型  正确标记  输入  正确单词  xxx秒后再试  音标  汉语 记忆持久力变化
    card_type=serializers.SerializerMethodField()
    is_ok=serializers.SerializerMethodField()
    word_input=serializers.SerializerMethodField()
    later_time=serializers.SerializerMethodField()
    english=serializers.CharField(source='english_obj.english')
    pronunciation=serializers.CharField(source='english_obj.pronunciation')
    chinese=serializers.CharField(source='english_obj.chinese')

    def get_is_ok(self,log_obj):
        view_obj=get_view_from_serializer(self)
        return view_obj.is_ok

    def get_card_type(self,log_obj):
        view_obj=get_view_from_serializer(self)
        return view_obj.card_type

    def get_word_input(self,log_obj):
        view_obj=get_view_from_serializer(self)
        return view_obj.word_input

    def get_later_time(self,log_obj):
        now_time=datetime.datetime.now()
        diff_time=log_obj.next_memory_time-now_time
        return str(diff_time)


    class Meta:
        model=EnglishWordRecordModel
        fields=('card_type','is_ok','word_input','later_time',
                'english','pronunciation','chinese','memory_power',)


















