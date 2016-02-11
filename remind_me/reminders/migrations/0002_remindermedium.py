# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderMedium',
            fields=[
                ('guid', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, db_index=True)),
                ('sms', models.BooleanField(default=False)),
                ('email', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reminder', models.OneToOneField(related_name='reminder', to='reminders.Reminder')),
            ],
        ),
    ]
