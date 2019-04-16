from rest_framework.routers import DefaultRouter
from app_main import views


app_main_router = DefaultRouter()
app_main_router.register(r'card', views.CardViewSet, base_name='app_main_card')
app_main_router.register(r'memory_card_commit', views.MemoryCardCommitViewSet, base_name='app_main_memory_card_commit')
app_main_router.register(r'strengthen_card_commit', views.StrengthenCardCommitViewSet,
                         base_name='app_main_strengthen_card_commit')
app_main_router.register(r'update_card_commit', views.UpdateCardCommitViewSet,
                         base_name='app_main_update_card_commit')
