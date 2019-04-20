from rest_framework.routers import DefaultRouter
from app_main import views

app_main_router = DefaultRouter()
app_main_router.register(r'index', views.IndexViewSet, base_name='app_main_index')
app_main_router.register(r'get_word_card', views.CardViewSet, base_name='app_main_get_word_card')
app_main_router.register(r'new_card_commit', views.NewCardCommitViewSet, base_name='app_main_new_card_commit')
app_main_router.register(r'strengthen_card_commit', views.StrengthenCardCommitViewSet,
                         base_name='app_main_strengthen_card_commit')
app_main_router.register(r'update_card_commit', views.UpdateCardCommitViewSet,
                         base_name='app_main_update_card_commit')
app_main_router.register(r'census', views.CensusViewSet, base_name='app_main_census')
