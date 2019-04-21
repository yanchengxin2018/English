from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.viewsets import GenericViewSet,mixins


#主页
class MainViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return render(request,'main/main.html')


#登录
class LogViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return render(request,'log/log.html')


#注册
class RegViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return render(request,'reg/reg.html')


#菜单
class IndexViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        if request.user:
            return render(request,'index/index.html')
        else:
            return HttpResponseRedirect('/url/main/')

#开始
class StartViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        if request.user:
            return render(request,'start/start.html')
        else:
            return HttpResponseRedirect('/url/main/')

#帮助
class HelpViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return render(request,'help/help.html')

#统计
class CensusViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        if request.user:
            return render(request,'census/census.html')
        else:
            return HttpResponseRedirect('/url/main/')

#交谈
class TalkViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        if request.user:
            return render(request,'talk/talk.html')
        else:
            return HttpResponseRedirect('/url/main/')


#退出
class ExitViewSet(GenericViewSet,mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        return render(request,'exit/exit.html')






