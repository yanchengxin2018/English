import datetime,random
from django.db.models import Q
from app_databases.models import StrengthenMemoryModel,EnglishWordRecordModel,EnglishWordModel
from app_main.serializers import StrengthenCardSerializer,EnglishWordRecordCardSerialzer,EnglishWordSerializer


# 得到一个单词
def get_english_word(user_obj):
    now_time = datetime.datetime.now()
    # 从记忆加强数据库得到单词
    #下次记忆时间大于当前时间的单词记录
    englishs_exact_obj=EnglishWordModel.objects.filter(strengthenmemorymodel__previous_memory_time__gt=now_time).distinct()
    #排除了那些下次记忆时间大于当前时间的所有单词
    strengthens_obj =StrengthenMemoryModel.objects.filter(~Q(english_obj__in=englishs_exact_obj))
    #从加强表查询数据  条件：当前用户/最迟时间小于当前

    strengthens_obj = strengthens_obj.filter(user_obj=user_obj,previous_memory_time__lt=now_time)
    if strengthens_obj:
        #下次记忆时间位于最早的时间线
        strengthen_obj = strengthens_obj.order_by('previous_memory_time').first()
        # 把记忆加强表的记录处理成数据
        serializer_obj = StrengthenCardSerializer(strengthen_obj)
        return serializer_obj.data


    # 从记忆历史数据库得到单词
    #排除了那些下次记忆时间大于当前时间的所有单词
    records_obj =EnglishWordRecordModel.objects.filter(~Q(english_obj__in=englishs_exact_obj))
    # 从记录表查询数据  条件：当前用户/最迟时间小于当前
    records_obj = records_obj.filter(user_obj=user_obj,previous_memory_time__lt=now_time)
    if records_obj:
        record_obj = records_obj.order_by('previous_memory_time').first()
        # 把历史记忆表的记录处理成数据
        serializer_obj = EnglishWordRecordCardSerialzer(record_obj)
        return serializer_obj.data

    # 从单词库随机抽取
    return english_obj_handler(user_obj)


# 从单词库随机抽取
def english_obj_handler(user_obj):
    # 从加强库以及历史库没有的词
    englishwords_obj = EnglishWordModel.objects.filter(Q(englishwordrecordmodel__user_obj=user_obj) |
                                                       Q(strengthenmemorymodel__user_obj=user_obj))
    englishwords_obj = EnglishWordModel.objects.filter(~Q(pk__in=englishwords_obj))
    count = englishwords_obj.count()
    obj_index = random.randint(0, count - 1)
    englishword_obj = englishwords_obj[obj_index]
    serializer_obj = EnglishWordSerializer(englishword_obj)
    return serializer_obj.data

