from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/Calculator_App/(?P<session_name>\w+)/$', consumers.CalcConsumer),
]