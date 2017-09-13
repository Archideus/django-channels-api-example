from django.db import models
from channels import Group
from accounts.models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save

import json

class Notification(models.Model):
    """
    Notifications
    """
    user = models.ForeignKey(UserProfile)
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)


