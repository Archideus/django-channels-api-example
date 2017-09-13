from channels_api.bindings import ResourceBinding

from .models import Notification
from .api.serializers import NotificationSerializer

class NotificationBinding(ResourceBinding):
    model = Notification
    stream = "notification"
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

