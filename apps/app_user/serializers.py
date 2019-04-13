from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app_user.models import UserModel,ReceiveFileModel
from app_exception import custom_exceptions



#注册
class RegSerializer(ModelSerializer):
    password=serializers.CharField(max_length=128,help_text='密码',write_only=True)

    class Meta:
        model=UserModel
        fields=('id','username','password','pet_name',)

    def create(self, validated_data):
        user_obj=super().create(validated_data)
        password=validated_data.get('password')
        user_obj.set_password(password)
        user_obj.save()
        return user_obj


#登录
class LogSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20,help_text='用户名')
    password=serializers.CharField(max_length=150,help_text='密码')

    def validate_username(self,username):
        user_obj=UserModel.objects.filter(username=username).first()
        if user_obj:
            return user_obj
        else:
            raise custom_exceptions.Status_404('用户不存在')

    def validate(self, attrs):
        user_obj=attrs.get('username')
        password=attrs.get('password')
        is_ok=user_obj.check_password(password)
        if not is_ok:raise custom_exceptions.Status_403('密码不正确')
        self.user_obj=user_obj
        return attrs


#接收文件
class ReceiveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReceiveFileModel
        fields=('id','file',)













