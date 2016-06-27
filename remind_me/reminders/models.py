import uuid

from django.db import models

from customers.models import Customer


class Reminder(models.Model):
    customer = models.ForeignKey(Customer, related_name='reminders', db_index=True)
    message = models.TextField()
    scheduled_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s<---->%s" %(self.guid, self.created_at)
