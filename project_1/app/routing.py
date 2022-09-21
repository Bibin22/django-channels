import imp
from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/wsc/', TestWebsocket.as_asgi())
]