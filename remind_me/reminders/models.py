import uuid

from django.db import models

from customers.models import Customer


class Reminder(models.Model):
    customer = models.ForeignKey(Customer, related_name='reminders', db_index=True)
    guid = models.UUIDField(db_index=True,primary_key=True,default=uuid.uuid4, editable=False)
    message = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s<---->%s" %(self.guid, self.created_at)

class ReminderMedium(models.Model):
    reminder = models.OneToOneField(Reminder, related_name='reminder', db_index=True)
    guid = models.UUIDField(db_index=True,primary_key=True,default=uuid.uuid4, editable=False)
    sms = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s<---->%s" %(self.guid, self.created_at)
