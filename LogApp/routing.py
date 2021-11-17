from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from Messenger import routing as messenger_routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(messenger_routing.websocket_urlpatterns)),
})
