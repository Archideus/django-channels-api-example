from django.db import models
from accounts.models import UserProfile
from django.utils import timezone

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

    
    """
    def save(self, *args, **kwargs):
        print('Saving...')
        if not self.created and not self.pk:
            self.created = timezone.now()
        super(Notification, self).save(*args, **kwargs)
    """

