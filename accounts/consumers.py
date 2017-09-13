import json
from channels import Channel
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
from channels.auth import channel_session_user_from_http, channel_session_user

from notifyme.models import Notification
from .models import UserProfile
from .exceptions import ClientError


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    message.channel_session['users'] = []

def ws_receive(message):
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("notification.receive").send(payload)
    print("Received")

@channel_session_user
def ws_disconnect(message):
    for user_key in message.channel_session.get("users", set()):
        try:
            user = UserProfile.objects.get(key=user_key)
            user.websocket_group.discard(message.reply_channel)
        except UserProfile.DoesNotExist:
            pass



class NotificationConsumer(JsonWebsocketConsumer):
    #strict_ordering = False
    #channel_session_user = True
    http_user = True

    def connection_groups(self, **kwargs):
        print("Connecting groups?")
        return ['test']

    def connect(self, message, **kwargs):
        print("Joining")
        print(str(message.get('user')))
        try:
            user = UserProfile.objects.get(key=message['user'])
        except UserProfile.DoesNotExist:
            return None
        
        user.send_notification('User %s Joined' % user.username)
        
        user.websocket_group.add(message.reply_channel)
        message.channel_session['users'] = list(set(message.channel_session['users']).union([user.key]))

        message.reply_channel.send({
            "text": json.dumps({
                "join": user.key,
                "user": user.username,
            }),
        })

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON message
        """
        print('Receiving...') 
        # Simple echo
        #self.send(message)
        if content['user'] not in message.channel_session['users']:
            print("Session Users")
            for user in message.channel_session['users']:
                print(user)
            raise ClientError("Client Error")
        try:
            user = UserProfile.objects.get(key=content['user'])
        except UserProfile.DoesNotExist:
            return None

        notification = Notification(user=user)
        notification.save()
        user.send_notification(message['message'])

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        try:
            user = UserProfile.objects.get(key=message['user'])
        except UserProfile.DoesNotExist:
            return None
        user.send_message('User %s leaving :(' % user.username)

        user.websocket_group.discard(message.reply_channel)

        message.reply_channel.send({
            "text": json.dumps({
                "leave": user.key,
                "user": user.username,
            })
        })

    """
    method_mapping = {
        'notifications':'join',
        'notifications':'leave',
        'notifications':'send',
    }

    def join(self, message, **kwargs):
        print("Joining")
        print(str(message.get('user')))
        try:
            user = UserProfile.objects.get(key=message['user'])
        except UserProfile.DoesNotExist:
            return None
        
        user.send_notification('User %s Joined' % user.username)
        
        user.websocket_group.add(message.reply_channel)
        message.channel_session['users'] = list(set(message.channel_session['users']).union([user.key]))

        message.reply_channel.send({
            "text": json.dumps({
                "join": user.key,
                "user": user.username,
            }),
        })


    def leave(self, message, **kwargs):
        room = get_room_or_error(message["room"], message.user)
        try:
            user = UserProfile.objects.get(key=message['user'])
        except UserProfile.DoesNotExist:
            return None
        user.send_message('User %s leaving :(' % user.username)

        user.websocket_group.discard(message.reply_channel)

        message.reply_channel.send({
            "text": json.dumps({
                "leave": user.key,
                "user": user.username,
            })
        })


    def send(self, message, **kwargs):
        if message['user'] not in message.channel_session['users']:
            print("Session Users")
            for user in message.channel_session['users']:
                print(user)
            raise ClientError("Client Error")
        try:
            user = UserProfile.objects.get(key=message['user'])
        except UserProfile.DoesNotExist:
            return None

        notification = Notification(user=user)
        notification.save()
        user.send_notification(message['message'])
    """


"""
@channel_session_user
def notification_send(message):


#@catch_client_error
@channel_session_user
def notification_join(message):

#@catch_client_error
@channel_session_user
def notification_leave(message):
"""
