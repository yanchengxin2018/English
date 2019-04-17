from rest_framework.viewsets import GenericViewSet as G, ModelViewSet
from rest_framework import mixins as M
from rest_framework.response import Response
from app_user.serializers import RegSerializer, LogSerializer
from app_user.models import UserModel
from app_user.app_user_tools import get_token_from_user


# 注册
class RegViewSet(G, M.CreateModelMixin, M.ListModelMixin):
    queryset = UserModel.objects.all().order_by('id')  # 临时的--查看所有用户
    serializer_class = RegSerializer


# 登录
class LogViewSet(G, M.CreateModelMixin):
    serializer_class = LogSerializer

    def create(self, request, *args, **kwargs):
        serializer_obj = LogSerializer(data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        self.user_obj = serializer_obj.user_obj
        token = get_token_from_user(self.user_obj)
        response_data = {'token': token, 'name': self.user_obj.pet_name, 'username': self.user_obj.username}
        response = Response(response_data)
        response.set_cookie('token', token)
        return response


# 查看当前登录用户
class NowUserViewSet(G, M.ListModelMixin):

    def list(self, request, *args, **kwargs):
        print('-->', request.user)
        return Response(request.user.pet_name)
