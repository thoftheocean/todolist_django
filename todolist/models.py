from django.db import models
import django.utils.timezone as timezone
from datetime import datetime

# Create your models here.
class Todolist(models.Model):
    event = models.CharField(max_length=300)
    status = models.CharField(max_length=50)
    timezone_now = models.DateTimeField(default=timezone.now)
    # timezone_utc = models.DateTimeField(default=timezone.utc)
    datetime_utcnow = models.DateTimeField(default=datetime.utcnow)
    datetime_now = models.DateTimeField(default=datetime.now)

