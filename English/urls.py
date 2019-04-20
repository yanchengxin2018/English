from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app_user.app_user_urls import app_user_router
from app_tools.app_tools_urls import app_tools_router
from app_main.app_main_urls import app_main_router
from app_talk.app_talk_urls import app_talk_router


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/',include(app_user_router.urls)),
    url(r'^tools/', include(app_tools_router.urls)),
    url(r'^main/', include(app_main_router.urls)),
    url(r'^talk/', include(app_talk_router.urls)),
]





