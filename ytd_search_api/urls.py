from django.conf.urls import url
from .views import YtdTemplateViewSet, YtdApiViewset


urlpatterns = [
    url(r'home', YtdTemplateViewSet.as_view(), name='home_page'),
    url(r'ytd/', YtdApiViewset.as_view(), name='ytd_api')
]
