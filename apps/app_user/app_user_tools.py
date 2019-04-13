from rest_framework_jwt.settings import api_settings


#用户实例转化为jwt-token编码
def get_token_from_user(user_obj=None):
    payload = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode = api_settings.JWT_ENCODE_HANDLER
    data = payload(user_obj) # 把用户表转化为字典
    token = jwt_encode(data) # 把字典转化为jwt字符串
    return token
