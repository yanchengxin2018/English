from rest_framework.routers import DefaultRouter
from app_tools import views


app_tools_router=DefaultRouter()
app_tools_router.register(r'make_word',views.MakeEnglishWordViewSet,base_name='app_tools_make_word')
app_tools_router.register(r'make_level',views.MakeLevelViewSet,base_name='app_tools_make_level')
app_tools_router.register(r'english_word',views.EnglishWordViewSet,base_name='app_tools_english_word')











