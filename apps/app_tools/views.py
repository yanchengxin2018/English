from rest_framework.viewsets import GenericViewSet as G,ModelViewSet
from rest_framework import mixins as M
from rest_framework.response import Response
from app_tools.serializers import MakeEnglishWordSerializer,EnglishWordSerializer
from app_databases.models import EnglishWordModel


#制作数据库
class MakeEnglishWordViewSet(G,M.ListModelMixin):

    def list(self, request, *args, **kwargs):
        with open('apps/app_tools/english_word.txt','r') as f:
            lines=f.readlines()
        index=1
        for line in lines:
            word_data=self.get_word_data(line)
            word_data['index']=index
            index+=1
            serializer_obj=MakeEnglishWordSerializer(data=word_data)
            serializer_obj.is_valid(raise_exception=True)
            serializer_obj.save()
            print('单词{}更新成功![{}]'.format(word_data.get('english'),index-1))
        return Response('成功')

    def get_word_data(self,line):
        # 1. abandon/ ə’bændən/ vt.丢弃；放弃，抛弃\n
        line=line.replace('[','/')
        line=line.replace(']','/')
        line=line.split('/')
        english=self.get_english(line[0])
        chinese=self.get_chinese(line[2])
        pronunciation=self.get_pronunciation(line[1])
        word_data={'english':english,'chinese':chinese,'pronunciation':pronunciation}
        return word_data

    def get_english(self,english):
        #1. abandon
        english=english.split('.')
        english=english[1].strip()
        return english

    def get_chinese(self,chinese):
        # vt.丢弃；放弃，抛弃\n
        chinese=chinese.strip()
        return chinese

    def get_pronunciation(self,pronunciation):
        # ə’bændən
        pronunciation=pronunciation.strip()
        return pronunciation


#查看词库列表
class EnglishWordViewSet(G,M.ListModelMixin):
    queryset = EnglishWordModel.objects.all().order_by('id')
    serializer_class = EnglishWordSerializer










