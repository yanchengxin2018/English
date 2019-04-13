from rest_framework.routers import DefaultRouter
from app_user import views


app_user_router=DefaultRouter()
app_user_router.register(r'reg',views.RegViewSet,base_name='app_user_reg')
app_user_router.register(r'log',views.LogViewSet,base_name='app_user_log')
app_user_router.register(r'who_im_i',views.Who_am_I_ViewSet,base_name='app_user_who_im_i')
app_user_router.register(r'receivefile',views.ReceiveViewSet,base_name='app_user_receivefile')


