                                                         REMIND ME
                                                         
RemindMe is a simple app that provides API for saving reminder.

For using this:

1. Clone the repo

2. Setup a mysql database(either use settings.py credentials or create your own in settings_local.py)

3. start the development server

4. Go to 127.0.0.1:8000/reminder/save/

5. Token authentication is being used, to access browsable api use ModHeader(google chrome extension)
to set authorization header for the request

6. API accepts 5 parameters : message, date(yyyy-mm-dd), time(hh:mm:ss), sms(true/false), email(true/false)

7. The date and time should be appropriate to represent any time in future and atleast one of the medium should be set to true
