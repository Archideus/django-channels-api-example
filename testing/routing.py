from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from notifyme.bindings import NotificationBinding

class APIDemultiplexer(WebsocketDemultiplexer):
    consumers = {
      'notification': NotificationBinding.consumer
    }

    # Adding groups to the websocket mutliplexer will
    # trigger two responses whenever data is pushed 
    # throught the socket but only one if the db is
    # updated thorugh other means.
    groups = [
        'notifyme.notification-create',
        'notifyme.notification-update',
        'notifyme.notification-destroy',
    ]

channel_routing = [
    route_class(APIDemultiplexer, path='^/stream/?$'),
]

