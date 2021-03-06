from django.conf import settings
from rest_framework.viewsets import GenericViewSet as G, ModelViewSet
from rest_framework import mixins as M
from rest_framework.response import Response
from app_tools.serializers import MakeEnglishWordSerializer, EnglishWordSerializer, LevelSerializer
from app_databases.models import EnglishWordModel, LevelModel
from app_tools.permissions import IsManagerPermission
from app_tools.serializers import ReceiveFileSerializer,IP2IPSerializer
from app_tools.models import ReceiveFileModel
import os


# 制作单词数据库
class MakeEnglishWordViewSet(G, M.ListModelMixin):
    permission_classes = (IsManagerPermission,)

    def list(self, request, *args, **kwargs):
        with open('apps/app_tools/english_word.txt', 'r') as f:
            lines = f.readlines()
        index = 1
        for line in lines:
            word_data = self.get_word_data(line)
            word_data['index'] = index
            index += 1
            serializer_obj = MakeEnglishWordSerializer(data=word_data)
            serializer_obj.is_valid(raise_exception=True)
            serializer_obj.save()
            print('单词{}更新成功![{}]'.format(word_data.get('english'), index - 1))
        return Response('成功')

    def get_word_data(self, line):
        # 1. abandon/ ə’bændən/ vt.丢弃；放弃，抛弃\n
        line = line.replace('[', '/')
        line = line.replace(']', '/')
        line = line.split('/')
        english = self.get_english(line[0])
        chinese = self.get_chinese(line[2])
        pronunciation = self.get_pronunciation(line[1])
        word_data = {'english': english, 'chinese': chinese, 'pronunciation': pronunciation}
        return word_data

    def get_english(self, english):
        # 1. abandon
        english = english.split('.')
        english = english[1].strip()
        return english

    def get_chinese(self, chinese):
        # vt.丢弃；放弃，抛弃\n
        chinese = chinese.strip()
        return chinese

    def get_pronunciation(self, pronunciation):
        # ə’bændən
        pronunciation = pronunciation.strip()
        return pronunciation


# 查看词库列表
class EnglishWordViewSet(G, M.ListModelMixin):
    queryset = EnglishWordModel.objects.all().order_by('id')
    serializer_class = EnglishWordSerializer


# 初始化记忆强度等级信息
class MakeLevelViewSet(G, M.ListModelMixin, M.CreateModelMixin):
    queryset = LevelModel.objects.all().order_by('level')
    serializer_class = LevelSerializer
    permission_classes = (IsManagerPermission,)

    def create(self, request, *args, **kwargs):
        LevelModel.objects.all().delete()
        for level in range(15):
            LEVEL = 'LEVEL_{}'.format(level)
            time_long = getattr(settings, LEVEL)
            cycle = self.get_cycle(level)
            LevelModel.objects.create(level=level, time_long=time_long, cycle=cycle)
        return Response('初始化完毕')

    # 获得周期字段
    def get_cycle(self, level):
        if level <= 4:
            return 'd'
        elif (level <= 9) and (level > 4):
            return 'z'
        else:
            return 'c'


# 收发文件
class ReceiveViewSet(ModelViewSet):
    queryset = ReceiveFileModel.objects.all().order_by('-created_at')
    serializer_class = ReceiveFileSerializer


#改变静态文件里的ip地址
class IP2IPViewSet(G,M.ListModelMixin,M.CreateModelMixin):
    queryset = ReceiveFileModel.objects.all().order_by('-created_at')
    serializer_class = IP2IPSerializer


    def list(self, request, *args, **kwargs):
        path='static/HTML'
        ip_1=request.GET.get('ip_1',None)
        files=self.get_files(path)
        all_ips=self.get_all_ips(files,ip_1,)
        return Response({'count':len(all_ips),'all_ips':all_ips})

    def create(self, request, *args, **kwargs):
        ip_1=request.data.get('ip_1')
        ip_2=request.data.get('ip_2')
        user_setting_ip=request.data.get('user_setting_ip',False)
        if user_setting_ip:
            ip_2=settings.IP
        dir_name='static/HTML'
        files=self.get_files(dir_name)
        all_ips=self.get_all_ips(files,ip_1)
        all_ips_count=len(all_ips)
        for file in files:
            self.file_replace(file,ip_1,ip_2)

        return Response('{}-->{}(共{}处修改)'.format(ip_1,ip_2,all_ips_count))


    def get_files(self,dir_name):
        dir_or_file_list=os.listdir(dir_name)
        files=[]
        for dir_or_file in dir_or_file_list:
            path='{}/{}'.format(dir_name,dir_or_file)
            status=os.path.isdir(path)
            if status:
                files=files+self.get_files(path)
            else:
                files.append(path)
        html_js_files=[]
        for file in files:
            file_type=file.split('.')[-1]
            if file_type=='js' or file_type=='html' or file_type=='css':
                html_js_files.append(file)
        return html_js_files

    def get_all_ips(self,files,ip_1):
        all_ips=[]
        for file in files:
            lines=self.get_ip(file,ip_1,'')
            all_ips=all_ips+lines
        return all_ips

    def get_ip(self,file,ip_1,ip_2):
        lines=[]
        with open(file,'r') as f:
            datas=f.readlines()
            for data in datas:
                new_data=data.replace(ip_1,ip_2)
                if data != new_data:
                    lines.append(file+'-->'+data)
        return lines

    def file_replace(self,file,ip_1,ip_2):
        context=[]
        with open(file,'r') as f:
            datas=f.readlines()
            for data in datas:
                new_data=data.replace(ip_1,ip_2)
                context.append(new_data)
        with open(file,'w') as f:
            for line in context:
                f.write(line)
        return True





