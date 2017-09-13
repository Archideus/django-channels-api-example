from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from notifyme.bindings import NotificationBinding

class APIDemultiplexer(WebsocketDemultiplexer):
    consumers = {
      'notification': NotificationBinding.consumer
    }


channel_routing = [
    route_class(APIDemultiplexer, path='^/stream/?$'),
]

