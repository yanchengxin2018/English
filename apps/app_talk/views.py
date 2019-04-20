from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from app_talk.permissions import IsAuthPermission
from app_talk.serializers import TalkSerializer
from app_databases.models import TalkModel


class TalkViewSet(GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = (IsAuthPermission,)
    serializer_class = TalkSerializer
    queryset = TalkModel.objects.all().order_by('-commit_time')





