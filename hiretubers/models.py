from django.db import models
from datetime import datetime

# Create your models here.


class Hiretubers(models.Model):
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    tuber_id = models.IntegerField(),
    tuber_name = models.CharField(max_length=100),
    city = models.CharField(max_length=100),
    phone = models.CharField(max_length=100),
    #potentiallly need to remove "","
    state = models.CharField(max_length=100),
    message = models.TextField(blank=True),
    user_id = models.CharField(blank=True),
    state = models.CharField(max_length=100),
    created_date = models.DateTimeField(blank=True, default=datetime.now),

    def __self__ (self):
        return self.email