from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Merchants(models.Model):

    SUBSCRIPTION_TYPE_CHOICE = (
                        ('Yearly', 'Yearly'),
                        ('Trial', 'Trial')
                        )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sub_status = models.BooleanField(default=True)
    subscription_type=models.CharField(max_length=10,
                                        choices = SUBSCRIPTION_TYPE_CHOICE,
                                        default='Trial')
