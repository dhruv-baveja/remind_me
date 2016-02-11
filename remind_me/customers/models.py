import uuid
import logging

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)

"""
Customer model is used for extending user model i.e. to incorporate new fields and methods.
"""
class Customer(models.Model):

    guid =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    user = models.OneToOneField(User, db_index=True, related_name="customer")
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):

        return "%s<---->%s" %(self.guid, self.user)

"""
Post save for creating customer and token on saving user
"""
def create_customer(sender, instance, created, **kwargs):
    
    if created:

        customer, created = Customer.objects.get_or_create(user=instance)
        token = Token.objects.create(user=instance)
        logger.info("Created customer and token for user %s" %(instance))
    

post_save.connect(create_customer, sender=User)

