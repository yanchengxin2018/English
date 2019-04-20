import datetime
from django.conf import settings
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from app_exception import custom_exceptions
from app_databases.models import StrengthenMemoryModel, EnglishWordRecordModel
from app_main.serializers import MemoryCardCommitSerializer
from app_main.serializers import StrengthenCardCommitSerializer, UpdateCardCommitSerializer
from app_main.tools import log_update, get_card
from app_main.tools import is_exist_log, get_word_obj, log_lowwer
from app_main.tools import is_spell_right, get_next_memory_time, get_level_alter,later_time
from app_main.permissions import IsAuthPermission
from django.http import HttpResponseRedirect
from django.db.models import Max

# 得到一张卡片
class CardViewSet(GenericViewSet, mixins.ListModelMixin):
    permission_classes = (IsAuthPermission,)

    def list(self, request, *args, **kwargs):
        card = get_card(request.user)
        if not card:
            raise custom_exceptions.Status_404('当前时间没有产生新的卡片')
        return Response(card)


# 新卡片提交
class NewCardCommitViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = MemoryCardCommitSerializer
    permission_classes = (IsAuthPermission,)

    # 返回记忆卡或者测试卡
    def create(self, request, *args, **kwargs):
        word_index = self.request.data.get('word_index', None)
        word_obj = get_word_obj(word_index)
        user_obj = self.request.user
        self.record_update(word_obj)
        card = get_card(user_obj)
        return Response(card)

    def record_update(self, word_obj):
        user_obj = self.request.user
        record_obj = EnglishWordRecordModel.objects.filter(english_obj=word_obj).first()
        if record_obj:
            raise custom_exceptions.Status_403('单词已经存在于记录库,请通过record类型的卡片提交')
        log_update('update_card', user_obj, word_obj)


# 加强卡片提交
class StrengthenCardCommitViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = StrengthenCardCommitSerializer
    permission_classes = (IsAuthPermission,)

    def create(self, request, *args, **kwargs):
        user_obj = request.user
        card_type = 'strengthen_card'
        word_index = request.data.get('word_index', None)
        if not is_exist_log(user_obj=user_obj, card_type=card_type, word_index=word_index):
            raise custom_exceptions.Status_404('没有找到对应的卡片')
        data = self.strengthen_update()
        return Response(data)

    def strengthen_update(self):
        card_type = 'strengthen_card'
        spell = self.request.data.get('spell', None)
        word_index = self.request.data.get('word_index', None)
        user_obj = self.request.user
        is_right = is_spell_right(spell, word_index)
        word_obj = get_word_obj(word_index)
        ip=settings.IP
        if is_right:
            info_image = '{}/static/HTML/start/info_backs/right.jpg'.format(ip)
            user_word_strengthen_obj = StrengthenMemoryModel.objects.filter(
                english_obj__pk=word_index, user_obj=user_obj)
            strengthen_last_obj = user_word_strengthen_obj.order_by('created_at').last()

            highest_level = settings.STRENGTHEN_HIGHEST
            if strengthen_last_obj.level >= highest_level:
                user_word_strengthen_obj.delete()
                next_memory_time = '已结束记忆加强'
            else:
                log_update(card_type, user_obj, word_obj)
                next_memory_time = get_next_memory_time(card_type, user_obj, word_obj)
        else:
            info_image = '{}/static/HTML/start/info_backs/error.jpg'.format(ip)
            log_lowwer(card_type, user_obj, word_obj)
            next_memory_time = get_next_memory_time(card_type, user_obj, word_obj)
        level_alter = get_level_alter(card_type, user_obj, word_obj)
        data = {'card_type': 'info_card', 'word_index': word_index, 'spell': spell, 'is_right': is_right,
                'next_memory_time': next_memory_time, 'level_alter': level_alter,'info_image':info_image}
        return data


# 升级卡片提交
class UpdateCardCommitViewSet(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = UpdateCardCommitSerializer
    permission_classes = (IsAuthPermission,)

    def create(self, request, *args, **kwargs):
        user_obj = request.user
        card_type = 'update_card'
        word_index = request.data.get('word_index', None)
        if not is_exist_log(user_obj=user_obj, card_type=card_type, word_index=word_index):
            raise custom_exceptions.Status_404('没有找到对应的卡片')
        data = self.update_update()

        return Response(data)

    # 升级记录库
    def update_update(self):
        card_type = 'update_card'
        spell = self.request.data.get('spell', None)
        word_index = self.request.data.get('word_index', None)
        user_obj = self.request.user
        is_right = is_spell_right(spell, word_index)
        word_obj = get_word_obj(word_index)
        ip = settings.IP
        if is_right:
            info_image='{}/static/HTML/start/info_backs/right.jpg'.format(ip)
            log_update(card_type, user_obj, word_obj)
            next_memory_time = get_next_memory_time(card_type, user_obj, word_obj)
        else:
            info_image = '{}/static/HTML/start/info_backs/error.jpg'.format(ip)
            log_lowwer(card_type, user_obj, word_obj)
            next_memory_time = get_next_memory_time(card_type, user_obj, word_obj)
        level_alter = get_level_alter(card_type, user_obj, word_obj)
        word_obj=get_word_obj(word_index)
        data = {'card_type': 'info_card', 'word_index': word_index, 'spell': spell, 'is_right': is_right,
                'next_memory_time': next_memory_time, 'level_alter': level_alter,'info_image':info_image,
                'english':word_obj.english,'chinese':word_obj.chinese,'pronunciation':word_obj.pronunciation}
        if next_memory_time - datetime.datetime.now() > datetime.timedelta(days=30):
            log_update('strengthen_card', user_obj, word_obj)
        data['next_memory_time']=later_time(next_memory_time)
        return data


#跳转到主页
class IndexViewSet(GenericViewSet):

    def list(self, request, *args, **kwargs):
        if request.user:
            return HttpResponseRedirect('/static/HTML/index/index.html')
        else:
            return HttpResponseRedirect('/static/HTML/main/main.html')


#统计
class CensusViewSet(GenericViewSet,mixins.ListModelMixin):
    permission_classes = (IsAuthPermission,)

    def list(self, request, *args, **kwargs):
        data={}

        group = EnglishWordRecordModel.objects.filter(user_obj=request.user).values(
            'english_obj').annotate(created_at=Max('created_at'))

        created_ats = {data.get('created_at') for data in group}

        records_obj = EnglishWordRecordModel.objects.filter(created_at__in=created_ats)
        temp=0
        for i in range(15):
            count=records_obj.filter(level=i).count()
            data[i]=count
            temp+=count
        from app_databases.models import EnglishWordModel
        word_sum=EnglishWordModel.objects.all().count()
        data['word_sum']=word_sum
        data['residue'] = word_sum-temp
        data['name'] = request.user.username
        return Response(data)


# 得到最后一次更新的集合
# 从这个集合里筛选数量
