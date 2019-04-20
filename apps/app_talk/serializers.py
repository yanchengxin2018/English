from rest_framework import serializers
from app_databases.models import TalkModel


class TalkSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source='user_obj.username',read_only=True)
    myself=serializers.SerializerMethodField()

    def get_myself(self,talk_obj):
        if talk_obj.user_obj==self.get_user_obj():
            return True
        else:
            return False

    class Meta:
        model=TalkModel
        fields=('name','commit_time','context','myself',)

    def create(self, validated_data):
        validated_data['user_obj']=self.get_user_obj()
        return super().create(validated_data)

    def get_user_obj(self):
        view = self.context.get('view')
        user_obj=view.request.user
        return user_obj


