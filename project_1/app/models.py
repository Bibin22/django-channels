import json

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        un_seen = Notifications.objects.filter(is_seen=False).count()
        data = {'count':un_seen, 'current_notification':self.notification}
        async_to_sync(channel_layer.group_send)(
            'test_room_group_name',{
                'type':'send_notification',
                'value':json.dumps(data),
            })

        super(Notifications, self).save(*args, **kwargs)
        print("HI")
