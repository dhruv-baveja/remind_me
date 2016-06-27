import datetime
import pytz

from rest_framework import serializers

from reminders.models import Reminder
from generic.utils import convert_date_time_to_iso_format


class ReminderSerializer(serializers.Serializer):

    message = serializers.CharField(max_length=250)
    scheduled_datetime = serializers.DateTimeField()
    phone_number = serializers.CharField(max_length=15, allow_null=True)

    @staticmethod
    def validate(data):
        if data['scheduled_datetime'] <= (datetime.datetime.now().replace(tzinfo=pytz.UTC) +
                                          datetime.timedelta(seconds=30)):
            raise serializers.ValidationError("You cannot set reminder for past")
        return data

    @staticmethod
    def update(instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.scheduled_datetime = validated_data.get('scheduled_datetime', instance.scheduled_datetime)
        if validated_data.get('phone_number'):
            customer = instance.customer
            customer.phone = validated_data.get('phone_number', customer.phone)
            customer.save()
        instance.save()
        return instance

    @staticmethod
    def create(validated_data):
        reminder = Reminder()
        reminder.customer = validated_data['customer']
        reminder.message = validated_data.get('message')
        reminder.scheduled_datetime = validated_data.get('scheduled_datetime')
        reminder.save()
        if validated_data.get('phone_number'):
            customer = validated_data['customer']
            customer.phone = validated_data.get('phone_number', customer.phone)
            customer.save()
        return reminder

    @staticmethod
    def to_representation(instance):
        reminder = {"phone_number": instance.customer.phone, "message": instance.message,
                    "scheduled_datetime": convert_date_time_to_iso_format(instance.scheduled_datetime),
                    "id": instance.id}
        return reminder

