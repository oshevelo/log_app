from Messenger import consumers
from django.urls import path

from django.conf.urls import url

websocket_urlpatterns = [
    url(r'^ws$', consumers.ChatConsumer.as_asgi()),
]