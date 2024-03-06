from django.db import models


class Reminders(models.Model):
    message = models.TextField(null=False, blank=False, max_length=1000)
    remind_date = models.DateField(blank=False, null=False)
    remind_time = models.TimeField(blank=False, null=False)