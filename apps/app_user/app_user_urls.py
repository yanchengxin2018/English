from rest_framework.routers import DefaultRouter
from app_user import views


app_user_router=DefaultRouter()
app_user_router.register(r'reg',views.RegViewSet,base_name='app_user_reg')
app_user_router.register(r'log',views.LogViewSet,base_name='app_user_log')
app_user_router.register(r'logout',views.LogOutViewSet,base_name='app_user_logout')
app_user_router.register(r'now_user',views.NowUserViewSet,base_name='app_user_now_user')



