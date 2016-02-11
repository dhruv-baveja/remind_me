from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


"""
This test class is for testing save_reminder api
"""
class SaveReminderTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user("test_user", "test@user.com", "123456")
        cls.token = cls.test_user.auth_token.key

    # this test case tests for an authenticated and valid request
    def test_request_token_authentication(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {
                "message" : "test message",
                "date" : "2016-07-14",
                "time" : "08:00:00",
                "sms" : True,
                "email" : True
                }
        response = client.post('/reminder/save/',data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    # this test case tests for unauthenticated request
    def test_request_without_authentication(self):
        client = APIClient()
        data = {
                "message" : "test message",
                "date" : "2016-07-14",
                "time" : "08:00:00",
                "sms" : True,
                "email" : True
                }
        response = client.post('/reminder/save/',data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # this test case tests that api doesn't allow past date and time
    def test_appropriate_date_and_time(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {
                "message" : "test message",
                "date" : "2015-07-14",
                "time" : "08:00:00",
                "sms" : True,
                "email" : True
                }
        response = client.post('/reminder/save/',data, format='json')
        expected_response = {
                                "non_field_errors": [
                                    "Please select a suitable date and time"
                                ]
                            }
        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # this test case tests that atleast one medium is to be selected for setting reminder
    def test_atleast_one_medium(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        data = {
                "message" : "test message",
                "date" : "2015-07-14",
                "time" : "08:00:00",
                "sms" : False,
                "email" : False
                }
        response = client.post('/reminder/save/',data, format='json')
        expected_response = {
                                "non_field_errors": [
                                    "Atleast select 1 medium for receiving reminder"
                                ]
                            }
        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
