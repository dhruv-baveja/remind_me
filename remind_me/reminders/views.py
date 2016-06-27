import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from reminders.serializers import ReminderSerializer
from reminders.models import Reminder
from generic.utils import get_data_from_request

logger = logging.getLogger(__name__)


class Reminders(APIView):

    @staticmethod
    def post(request):
        data = get_data_from_request(request)
        serializer = ReminderSerializer(data=data)
        customer = request.user.customer

        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error("Invalid data in request from {0} : {1}".format(customer, serializer.errors))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, id=None):
        if id is None:
            reminders = request.user.customer.reminders.all()
            serializer = ReminderSerializer(reminders, many=True)
            return Response(data=serializer.data)

        else:
            try:
                reminder = Reminder.objects.get(id=int(id))
            except Reminder.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                if request.user.customer == reminder.customer:
                    serializer = ReminderSerializer(reminder)
                    return Response(data=serializer.data)
                return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def delete(request, id):
        try:
            reminder = Reminder.objects.get(id=int(id))
        except Reminder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:

            if request.user.customer == reminder.customer:
                reminder.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def put(request, id):
        try:
            reminder = Reminder.objects.get(id=int(id))
        except Reminder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user.customer == reminder.customer:
                data = get_data_from_request(request)
                serializer = ReminderSerializer(instance=reminder, data=data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_403_FORBIDDEN)
