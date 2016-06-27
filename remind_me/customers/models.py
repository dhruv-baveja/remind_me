import logging

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


class Customer(models.Model):
    user = models.OneToOneField(User, db_index=True, related_name="customer")
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s<---->%s" %(self.guid, self.user)


def create_customer(sender, instance, created, **kwargs):
    if created:
        customer, created = Customer.objects.get_or_create(user=instance)
        logger.info("Created customer for user {0}" .format(instance))

post_save.connect(create_customer, sender=User)


def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        logger.info("Created token for user {0}" .format(instance))

post_save.connect(create_token, sender=User)

