from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app_user.app_user_urls import app_user_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/',include(app_user_router.urls)),
]





