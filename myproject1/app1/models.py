from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal
OFFER_TYPE_CHOICE = (
                        ('Percentage', 'Percentage Based Discount'),
                        ('Dollar', 'Dollar Value Discount'),
                        ('Shipping', 'Free Shipping'),
                        ('Gift', 'Free Gift')
                        )
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
class Products(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    uploaded_on=models.DateTimeField(default=datetime.now, blank=True)
    quantity=models.IntegerField(default=0)
    product_cost= models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    deliver_charges=models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    return_allowed=models.BooleanField(default=True)
    return_within=models.IntegerField(default=0)
    product_speficication=models.TextField(default=0)
    material_speficication=models.TextField(default=0)

class Merchant_Products(models.Model):
    merchant_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products)

class Categories(models.Model):
    category=models.CharField(max_length=100,unique=True)
    category_parent=models.CharField(max_length=100,default='NULL')

class Product_Category(models.Model):
    product = models.ForeignKey(Products)
    product_cat=models.ForeignKey(Categories)

class Offers(models.Model):    
    offer_title=models.CharField(max_length=100)
    offer_type=models.CharField(max_length=100,
                                        choices = OFFER_TYPE_CHOICE,
                                        default='NULL')
    created_on=models.DateTimeField(default=datetime.now, blank=True)
    valid_till=models.IntegerField(default=0)
    discount_amt=models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    is_active=models.BooleanField(default=True)
    offer_status = models.BooleanField(default=True)
    product_offer=models.ForeignKey(Products)

class Product_color_images(models.Model):      
    color_code=models.CharField(max_length=50,default='NULL')
    images = models.ImageField(blank=True)
    product_images=models.ForeignKey(Products)    

class emailverify(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=50)
    registration_time= models.DateTimeField(default=datetime.now, blank=True)
    def is_registered_recently(self):
         cur_time = timezone.now()
         return cur_time - datetime.timedelta(days=1) <= self.pub_date <= cur_time  
