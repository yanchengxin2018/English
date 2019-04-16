
import datetime
import random
from django.db.models import Q
from django.conf import settings
from app_databases.models import StrengthenMemoryModel, EnglishWordRecordModel, EnglishWordModel
from app_main.serializers import StrengthenCardSerializer, EnglishWordSerializer
from app_main.serializers import UpdateCardSerializer
from app_exception import custom_exceptions


# 得到一张单词卡(加强卡/升级卡/记忆卡)
def get_card(user_obj):
    card = get_strengthens_card(user_obj)
    if card:
        return card
    card = get_update_card(user_obj)
    if card:
        return card
    card = get_memory_card(user_obj)
    if card:
        return card


# 得到一张加强卡
def get_strengthens_card(user_obj):
    strengthen_obj = StrengthenMemoryModel.objects.filter(user_obj=user_obj).order_by('created_at').last()
    if not strengthen_obj:
        return None
    now_time = datetime.datetime.now()
    if strengthen_obj.next_memory_time < now_time:
        serializer_obj = StrengthenCardSerializer(strengthen_obj)
        return serializer_obj.data
    else:
        return None


# 得到一张升级卡
def get_update_card(user_obj):


    from django.db.models import Max
    a=EnglishWordRecordModel.objects.filter(user_obj=user_obj).values(
        'english_obj').annotate(bbb=Max('created_at'))
    print('-->',a)
    b=a.order_by('next_memory_time')
    print('--->', b)


    record_obj = EnglishWordRecordModel.objects.filter(user_obj=user_obj).order_by('next_memory_time').last()
    if not record_obj:
        return None
    now_time = datetime.datetime.now()
    if record_obj.next_memory_time < now_time:
        serializer_obj = UpdateCardSerializer(record_obj)
        return serializer_obj.data
    else:
        return None


# 得到一张记忆卡
def get_memory_card(user_obj):
    # 从加强库以及历史库没有的词
    englishwords_obj = EnglishWordModel.objects.filter(Q(englishwordrecordmodel__user_obj=user_obj) |
                                                       Q(strengthenmemorymodel__user_obj=user_obj))
    englishwords_obj = EnglishWordModel.objects.filter(~Q(pk__in=englishwords_obj))
    if not englishwords_obj:
        return None
    count = englishwords_obj.count()
    obj_index = random.randint(0, count - 1)
    englishword_obj = englishwords_obj[obj_index]
    serializer_obj = EnglishWordSerializer(englishword_obj)
    return serializer_obj.data


# 更新记录库-升级
def log_update(card_type, user_obj, word_obj):
    if card_type == 'update_card':
        record_obj = EnglishWordRecordModel.objects.filter(
            user_obj=user_obj, english_obj=word_obj).order_by('created_at').last()
        if not record_obj:
            seconds = getattr(settings, 'LEVEL_{}'.format(0))
            next_memory_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': 0, 'next_memory_time': next_memory_time}
            EnglishWordRecordModel.objects.create(**data)
        else:
            previous_memory_time = record_obj.next_memory_time
            previous_level = record_obj.level
            if previous_level < 14:
                level = previous_level + 1
            else:
                level = 14

            seconds = getattr(settings, 'LEVEL_{}'.format(level))
            next_memory_time = previous_memory_time + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': level, 'next_memory_time': next_memory_time}
            EnglishWordRecordModel.objects.create(**data)
    elif card_type == 'strengthen_card':
        strengthen_obj = StrengthenMemoryModel.objects.filter(
            user_obj=user_obj, word_obj=word_obj).order_by('created_at').last()
        if not strengthen_obj:
            seconds = getattr(settings, 'LEVEL_{}'.format(0))
            next_memory_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': 0, 'next_memory_time': next_memory_time}
            StrengthenMemoryModel.objects.create(**data)
        else:
            previous_memory_time = strengthen_obj.next_memory_time
            previous_level = strengthen_obj.level
            if previous_level < 5:
                level = previous_level + 1
            else:
                level = 5

            seconds = getattr(settings, 'LEVEL_{}'.format(level))
            next_memory_time = previous_memory_time + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': level, 'next_memory_time': next_memory_time}
            StrengthenMemoryModel.objects.create(**data)
    else:
        raise custom_exceptions.Status_400('未能识别的卡片类型')


# 更新记录库-降级
def log_lowwer(card_type, user_obj, word_obj):
    if card_type == 'update_card':
        record_obj = EnglishWordRecordModel.objects.filter(
            user_obj=user_obj, word_obj=word_obj).order_by('created_at').last()
        if not record_obj:
            seconds = getattr(settings, 'LEVEL_{}'.format(0))
            next_memory_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': 0, 'next_memory_time': next_memory_time}
            EnglishWordRecordModel.objects.create(**data)
        else:
            previous_memory_time = record_obj.next_memory_time
            previous_level = record_obj.level
            if previous_level > 0:
                level = previous_level - 1
            else:
                level = 0
            seconds = getattr(settings, 'LEVEL_{}'.format(level))
            next_memory_time = previous_memory_time + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': level, 'next_memory_time': next_memory_time}
            EnglishWordRecordModel.objects.create(**data)
    elif card_type == 'strengthen_card':
        strengthen_obj = StrengthenMemoryModel.objects.filter(
            user_obj=user_obj, word_obj=word_obj).order_by('created_at').last()
        if not strengthen_obj:
            seconds = getattr(settings, 'LEVEL_{}'.format(0))
            next_memory_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': 0, 'next_memory_time': next_memory_time}
            StrengthenMemoryModel.objects.create(**data)
        else:
            previous_memory_time = strengthen_obj.next_memory_time
            previous_level = strengthen_obj.level
            if previous_level > 0:
                level = previous_level - 1
            else:
                level = 0

            seconds = getattr(settings, 'LEVEL_{}'.format(level))
            next_memory_time = previous_memory_time + datetime.timedelta(seconds=seconds)
            data = {'user_obj': user_obj, 'english_obj': word_obj, 'level': level, 'next_memory_time': next_memory_time}
            StrengthenMemoryModel.objects.create(**data)


# 得到下次测试时间
def get_next_memory_time(card_type, user_obj, word_obj):
    if card_type == 'update_card':
        record_obj = EnglishWordRecordModel.objects.filter(
            user_obj=user_obj, english_obj=word_obj).order_by('created_at').last()
        if not record_obj:
            raise custom_exceptions.Status_503('服务器繁忙,请稍后再试')
        else:
            next_memory_time = record_obj.next_memory_time
            return next_memory_time
    elif card_type == 'strengthen_card':
        strengthen_obj = StrengthenMemoryModel.objects.filter(
            user_obj=user_obj, word_obj=word_obj).order_by('created_at').last()
        if not strengthen_obj:
            raise custom_exceptions.Status_503('服务器繁忙,请稍后再试')
        else:
            next_memory_time = strengthen_obj.next_memory_time
            return next_memory_time


# 得到单词级别变化信息
def get_level_alter(card_type, user_obj, word_obj):
    if card_type == 'update_card':
        logs_obj = EnglishWordRecordModel.objects.filter(
            user_obj=user_obj, english_obj=word_obj).order_by('-created_at')
    elif card_type == 'strengthen_card':
        logs_obj = StrengthenMemoryModel.objects.filter(
            user_obj=user_obj, word_obj=word_obj).order_by('-created_at')
    else:
        raise custom_exceptions.Status_400('card_type不能被理解')

    if len(logs_obj) == 0:
        raise custom_exceptions.Status_400('没有记录')
    elif len(logs_obj) == 1:
        log_obj = logs_obj.first()
        return '级别{}-->级别{}'.format(log_obj.level, log_obj.level)
    else:
        return '级别{}-->级别{}'.format(logs_obj[1].level, logs_obj[0].level)


# 当前用户的当前单词是否存在于记录中
def is_exist_log(user_obj, card_type, word_index):
    try:
        int(word_index)
    except Exception:
        raise custom_exceptions.Status_400("期望从index得到一个数字")

    if card_type == 'update_card':
        record_obj = EnglishWordRecordModel.objects.filter(user_obj=user_obj, english_obj__pk=word_index).first()
        return bool(record_obj)
    elif card_type == 'strengthen_card':
        strengthen_obj = StrengthenMemoryModel.objects.filter(user_obj=user_obj, english_obj__pk=word_index).first()
        return bool(strengthen_obj)
    else:
        raise custom_exceptions.Status_400("期望从'card_type'返回一个'update_card' 或 'strengthen_card'")


# 拼写是否正确
def is_spell_right(spell, word_index):
    try:
        word_obj = EnglishWordModel.objects.filter(pk=word_index).first()
    except Exception:
        raise custom_exceptions.Status_400('服务器无法理解word_index参数')
    return word_obj.english == spell


# 通过索引得到单词对象
def get_word_obj(word_index):
    word_obj = EnglishWordModel.objects.filter(pk=word_index).first()
    if not word_obj:
        raise custom_exceptions.Status_404('没有找到这个单词')
    return word_obj
