from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
SUBSCRIPTION_TYPE_CHOICE = (
                        ('Yearly', 'Yearly'),
                        ('Trial', 'Trial')
                        )
class Merchants(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sub_status = models.BooleanField(default=True)
    subscription_type=models.CharField(max_length=10,
                                        choices = SUBSCRIPTION_TYPE_CHOICE,
                                        default='Trial')
class emailverify(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=50)
    registration_time= models.DateTimeField(default=datetime.now, blank=True)
    def is_registered_recently(self):
         cur_time = timezone.now()
         return cur_time - datetime.timedelta(days=1) <= self.pub_date <= cur_time
  