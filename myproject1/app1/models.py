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


from datetime import datetime

# Create your models here.

 
class emailverify(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=50)
    registration_time= models.DateTimeField(default=datetime.now, blank=True)

    def is_registered_recently(self):
         cur_time = timezone.now()
         return cur_time - datetime.timedelta(days=1) <= self.pub_date <= cur_time
    
    

