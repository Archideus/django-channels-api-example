from channels.routing import route, route_class
from channels.staticfiles import StaticFilesConsumer
from . import consumers
 
channel_routing = [
    route_class(consumers.NotificationConsumer,  path=r"^notifications/"),
]

"""
websocket_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_receive),
    route("websocket.disconnect", consumers.ws_disconnect),
]   

custom_routing = [
    consumers.NotificationConsumer.as_route(path=r"^"),
]
"""
"""


custom_routing = [
    route("notification.receive", notification_send, command="^send$"),
    route("notification.receive", notification_join, command="^join$"),
    route("notification.receive", notification_leave, command="^leave$"),
]
"""

