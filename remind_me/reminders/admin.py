from django.contrib import admin

from reminders.models import Reminder, ReminderMedium

class ReminderAdmin(admin.ModelAdmin):

    list_display = ('guid', 'customer', 'message', 'date', 'time', 'created_at', 'updated_at')

    search_fields = ['guid', 'date', 'time', 'created_at', 'updated_at']

admin.site.register(Reminder, ReminderAdmin)


class ReminderMediumAdmin(admin.ModelAdmin):

    list_display = ('guid', 'reminder', 'email', 'sms', 'created_at', 'updated_at')

    search_fields = ['guid', 'created_at', 'updated_at']

admin.site.register(ReminderMedium, ReminderMediumAdmin)
