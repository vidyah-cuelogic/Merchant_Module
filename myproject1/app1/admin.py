from django.contrib import admin
from .models import Merchants,emailverify,Products,Categories,Product_Category,Offers,Product_color_images
# Register your models here.
admin.site.register(Merchants)
admin.site.register(emailverify)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Product_Category)
admin.site.register(Offers)
admin.site.register(Product_color_images)