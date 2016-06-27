from django.conf.urls import include, url
from reminders import views as reminders_views

urlpatterns = [
    url(r'^reminders/(?P<id>[0-9]+)/$', reminders_views.Reminders.as_view()),
    url(r'^reminders/$', reminders_views.Reminders.as_view()),
]
