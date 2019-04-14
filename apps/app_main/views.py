import datetime
from rest_framework.viewsets import GenericViewSet as G
from rest_framework import mixins as M
from rest_framework.response import Response
from app_main.tools import get_english_word
from app_main.serializers import EnglishWordRecordSerializer,EnglishWordRecordViewSetSerializer
from app_databases.models import EnglishWordModel
from app_exception import custom_exceptions


#无参数提交并获得数据
class StartViewSet(G,M.ListModelMixin):

    def list(self, request, *args, **kwargs):
        english_data = get_english_word(request.user)
        return Response(english_data)


#通过记忆卡片提交并获得数据
class MemoryCardCommitViewSet(G,M.CreateModelMixin):
    serializer_class = EnglishWordRecordViewSetSerializer
    #返回记忆卡或者测试卡
    def create(self, request, *args, **kwargs):
        user_obj=request.user
        english_obj=request.data.get('index',None)
        previous_memory_time=datetime.datetime.now()
        next_memory_time=previous_memory_time+datetime.timedelta(seconds=5)
        memory_power=5
        data={'user_obj':user_obj.id,'english_obj':english_obj,'previous_memory_time':previous_memory_time,
         'next_memory_time':next_memory_time,'memory_power':memory_power}
        serializer_obj=EnglishWordRecordSerializer(data=data)
        serializer_obj.is_valid(raise_exception=True)
        serializer_obj.save()
        english_data = get_english_word(request.user)
        return Response(english_data)


#通过测试卡提交并获得数据
class TestCardCommitViewSet(G,M.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        self.word_obj=self.get_word_obj()
        self.card_type=request.data.get('card_type',None)
        if not self.card_type:raise custom_exceptions.Status_400('card_type是必须的')
        if self.input_is_ok():
            data=self.word_level_up()
        else:
            data=self.word_level_low()
        return Response(data)

    #判断输入是否正确
    def input_is_ok(self):
        word_obj=self.word_obj
        word_input=self.request.post.get('word_input',None)
        if word_obj.english!=word_input:
            return False
        else:
            return True

    def get_word_obj(self):
        index = self.request.post.get('index', None)
        if not index:raise custom_exceptions.Status_400('index参数是必须的')
        word_obj=EnglishWordModel.objects.filter(pk=index).first()
        if not word_obj:raise custom_exceptions.Status_404('没有找到这个资源')
        return word_obj

    #单词级别升级
    def word_level_up(self):
        from app_databases.models import StrengthenMemoryModel,EnglishWordRecordModel
        # card_type  'strengthen'   'record'
        if self.card_type=='strengthen':
            log_model=StrengthenMemoryModel
        elif self.card_type=='record':
            log_model=EnglishWordRecordModel
        else:
            raise custom_exceptions.Status_400("'card_type' only use 'strengthen' or 'record' !")
        log_obj=log_model.objects.filter(english_obj=self.word_obj).order_by('-created_at').first()

        memory_power=log_obj.memory_power*5
        user_obj=self.request.user
        english_obj=self.word_obj
        previous_memory_time=datetime.datetime.now()
        next_memory_time=previous_memory_time+datetime.timedelta(seconds=memory_power)
        data={'user_obj':user_obj,'english_obj':english_obj,'previous_memory_time':previous_memory_time,
              'next_memory_time':next_memory_time,'memory_power':memory_power}
        log_model.objects.create(**data)
        # 记忆类型  正确标记  错误单词  正确单词  xxx秒后再试  音标  汉语 记忆持久力变化


    #单词级别下降
    def word_level_low(self):
        pass








