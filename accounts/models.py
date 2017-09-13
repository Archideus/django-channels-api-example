from django.db import models
from django.contrib.auth.models import AbstractUser  # this import allows us to get all the fields from the default user from django
from channels import Group
import json
from uuid import uuid4



class UserProfile(AbstractUser):
    key = models.CharField(unique=True,default=uuid4,max_length=64)

    @property
    def websocket_group(self):
        return Group("user-%s" % self.key)

    def send_notification(self,message):
        final_msg = {'user': self.key,'message':message}
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )
        print("Sending notification")

