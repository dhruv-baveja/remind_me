import datetime

from rest_framework import serializers

"""
This serializer is used by save_reminder view, to serialize incoming data
"""
class SaveReminderSerializer(serializers.Serializer):
    
    message = serializers.CharField(allow_blank=False, required=True)
    date = serializers.DateField(required=True, format="%Y-%m-%d")
    time = serializers.TimeField(required=True, format="%H:%M:%S")
    sms = serializers.BooleanField(required=True)
    email = serializers.BooleanField(required=True)

    """
    This method ensures that the reminder being set is for future only and
    atleast one medium is being selected
    """
    def validate(self, data):
        if data['sms'] == data['email'] == False:
            
            raise serializers.ValidationError("Atleast select 1 medium for receiving reminder")
        
        elif (data['date'] <= datetime.date.today() and 
            data['time'] < (datetime.datetime.now() + datetime.timedelta(minutes=1)).time()):
            
            raise serializers.ValidationError("Please select a suitable date and time")
        
        return data