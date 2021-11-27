from Messenger import consumers
from django.urls import path

from django.conf.urls import url

websocket_urlpatterns = [
    url(r'^ws/(?P<chat_group_id>\w+)/$', consumers.ChatConsumer),
]