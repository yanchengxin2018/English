from rest_framework.routers import DefaultRouter
from app_talk import views

app_talk_router=DefaultRouter()
app_talk_router.register(r'talk',views.TalkViewSet,basename='app_talk_talk')
