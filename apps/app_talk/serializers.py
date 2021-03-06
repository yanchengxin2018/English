from rest_framework import serializers
from app_databases.models import TalkModel
import datetime



class TalkSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user_obj.username', read_only=True)
    myself = serializers.SerializerMethodField()
    commit_time = serializers.SerializerMethodField()


    def get_commit_time(self, talk_obj):
        now_time = datetime.datetime.now()

        diff = now_time - talk_obj.commit_time
        seconds = diff.seconds
        d = seconds // (3600 * 24)
        h = seconds % (3600 * 24) // 3600
        m = seconds % 3600 // 60
        s = seconds % 60
        info = []
        if s:
            info.append('{}秒'.format(s))
        if m:
            info.append('{}分'.format(m))
        if h:
            info.append('{}时'.format(h))
        if d:
            info.append('{}天'.format(d))
        if len(info) >= 2:
            info = info[::-1][:2]
        info = ''.join(info)
        return '{}前'.format(info)

    def get_myself(self, talk_obj):
        if talk_obj.user_obj == self.get_user_obj():
            return True
        else:
            return False

    class Meta:
        model = TalkModel
        fields = ('name', 'commit_time', 'context', 'myself',)

    def create(self, validated_data):
        validated_data['user_obj'] = self.get_user_obj()
        return super().create(validated_data)

    def get_user_obj(self):
        view = self.context.get('view')
        user_obj = view.request.user
        return user_obj














