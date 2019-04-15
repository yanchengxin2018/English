from rest_framework.routers import DefaultRouter
from app_main import views


app_main_router=DefaultRouter()
app_main_router.register(r'start',views.StartViewSet,base_name='app_main_start')
app_main_router.register(r'memory_card_commit',views.MemoryCardCommitViewSet,base_name='app_main_memory_card_commit')
app_main_router.register(r'test_card_commit',views.TestCardCommitViewSet,base_name='app_main_test_card_commit')




