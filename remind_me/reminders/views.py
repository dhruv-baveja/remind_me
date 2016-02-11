import logging

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from serializers import SaveReminderSerializer
from utils import create_reminder_object, create_reminder_medium_object
from generic.utils import get_data_from_request

logger = logging.getLogger(__name__)

"""
This api view is used to save reminder
"""
@api_view(["POST"])
def save_reminder(request):

	data = get_data_from_request(request)
	serializer = SaveReminderSerializer(data=data)
	customer = request.user.customer

	logger.debug("Request to save reminder for customer : %s"%(customer))

	if serializer.is_valid():
		
		logger.debug("Request to save reminder for %s has valid data"%(customer))

		data = serializer.data

		reminder = create_reminder_object(data, customer)
		reminder_medium = create_reminder_medium_object(data, reminder)
		
		return Response(data, status=status.HTTP_201_CREATED)
	
	logger.error("Invalid data in request from %s : %s"%(customer, serializer.errors))

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)