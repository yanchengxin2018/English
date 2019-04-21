from rest_framework.routers import DefaultRouter
from app_url import views


app_url_router=DefaultRouter()
app_url_router.register(r'main',views.MainViewSet,basename='app_url_main')
app_url_router.register(r'reg',views.RegViewSet,basename='app_url_reg')
app_url_router.register(r'log',views.LogViewSet,basename='app_url_log')
app_url_router.register(r'index',views.IndexViewSet,basename='app_url_index')
app_url_router.register(r'start',views.StartViewSet,basename='app_url_start')
app_url_router.register(r'help',views.HelpViewSet,basename='app_url_help')
app_url_router.register(r'census',views.CensusViewSet,basename='app_url_census')
app_url_router.register(r'talk',views.TalkViewSet,basename='app_url_talk')
app_url_router.register(r'exit',views.ExitViewSet,basename='app_url_exit')




