import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings


#DRF的默认用户认证
class Authentication:

    def authenticate(self,request,*args,**kwargs):
        try:
            token=self.get_token(request)
            if not token:return(None,'token未携带或不正确')
            data=self.parse_token(token)
            self.data=data
            if not data:return(None,'不正确的token格式')
            if not self.valite_time(data):return (None,'token已过期')
            user_obj=self.get_user(data)
            return (user_obj,token)
        except:
            return (None,None)

    def get_user(self,data):
        username=data.get('username')
        user_model= get_user_model()
        user_obj=user_model.objects.filter(username=username).first()
        return user_obj

    def valite_time(self,data):
        #此刻
        now = datetime.datetime.now()
        #失效时间
        exp = data.get('exp')
        valite_range = datetime.datetime.utcfromtimestamp(exp)
        return valite_range > now

    def parse_token(self,token):
        decode_handler = api_settings.JWT_DECODE_HANDLER
        try:
            data=decode_handler(token)
            return data
        except:
            return None

    def get_token(self,request):
        auth=request.META.get('HTTP_AUTHORIZATION', b'')
        if auth:
            sign = settings.JWT_AUTH['JWT_AUTH_HEADER_PREFIX']
            try:
                token=auth.split(sign+' ')[1]
                return token
            except:
                return None
        else:
            auth = request.COOKIES.get('token', None)
            return auth




