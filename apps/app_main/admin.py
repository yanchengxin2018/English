from django.contrib import admin

# Register your models here.
from app_databases.models import EnglishWordRecordModel

admin.site.register([EnglishWordRecordModel])
