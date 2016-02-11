import logging

from reminders.models import Reminder, ReminderMedium

logger = logging.getLogger(__name__)

def create_reminder_object(data, customer):
	
	reminder = Reminder()
	reminder.message = data['message']
	reminder.time = data['time']
	reminder.date = data['date']
	reminder.customer = customer
	reminder.save()

	logger.debug("Reminder created : %s"%(reminder))

	return reminder

def create_reminder_medium_object(data, reminder):

	reminder_medium = ReminderMedium()
	reminder_medium.reminder = reminder
	reminder_medium.sms = data['sms']
	reminder_medium.email = data['email']
	reminder_medium.save()

	logger.debug("ReminderMedium created : %s"%(reminder_medium))

	return reminder_medium