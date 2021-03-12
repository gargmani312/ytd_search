# from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'', include(('ytd_search_api.urls', 'core_app'), namespace='app_1')),
]
