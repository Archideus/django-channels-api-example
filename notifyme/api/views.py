from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import views, viewsets, generics, filters
from rest_framework import parsers, renderers, exceptions
from rest_framework.permissions import AllowAny

from .serializers import NotificationSerializer
from ..models import Notification



class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    http_method_names = ['get', 'post', 'head'] # Only allow create

    def list(self, request):
        if self.request.user.is_authenticated():
            queryset = self.queryset.filter(user=self.request.user)
        else:
            queryset = self.queryset.none()
        return Response(self.serializer_class(queryset,many=True).data)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            serializer.validated_data['user'] = self.request.user
            serializer.save()


