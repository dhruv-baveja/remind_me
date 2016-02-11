from django.conf.urls import include, url
from reminders import views as reminders_views

urlpatterns = [
    url(r'^save/$', reminders_views.save_reminder),
]
