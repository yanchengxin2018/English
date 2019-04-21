from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from app_talk.permissions import IsAuthPermission
from app_talk.serializers import TalkSerializer
from app_databases.models import TalkModel
from django.contrib.auth import get_user_model


#聊天
class TalkViewSet(GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = (IsAuthPermission,)
    serializer_class = TalkSerializer
    queryset = TalkModel.objects.all().order_by('-commit_time')

    def list(self, request, *args, **kwargs):
        response=super().list(request, *args, **kwargs)
        response.data['user_count']=self.get_user_count()
        return response

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


    def get_user_count(self):
        UserModel = get_user_model()
        user_count = UserModel.objects.all().count()
        return user_count

