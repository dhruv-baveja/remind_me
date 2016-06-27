from django.contrib import admin

from reminders.models import Reminder


class ReminderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'message', 'scheduled_datetime', 'created_at', 'updated_at')

admin.site.register(Reminder, ReminderAdmin)
