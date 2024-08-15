import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns
from video_chat.routing import websocket_urlpatterns as video_chat_websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weconnect.settings')

# Combine WebSocket URL patterns from both chat and video_chat apps
websocket_urlpatterns = chat_websocket_urlpatterns + video_chat_websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
