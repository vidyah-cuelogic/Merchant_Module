from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from app1.models import emailverify
from datetime import datetime, timedelta
import hashlib
import os
import uuid
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from app1.forms import SignupForm,LoginForm,ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"app1/home.html",{})

    
def login(request):
    if request.method == 'GET':
            form = LoginForm()
            return render(request,"app1/login.html",{'form':form})
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
                print("plz")
                return render(request,"app1/dashboard.html")
        else:  
                return render(request,"app1/login.html",{'form':form})
    

def register(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            
            if form.is_valid()  :
                user = User.objects.create_user(form.cleaned_data['email'],form.cleaned_data['email'], form.cleaned_data['password']) 
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.is_active=False
                      
                user.save() 
                hash1 = str(uuid.uuid1()) 
                obj=user.emailverify_set.create(activation_key=hash1)
                subject="Welcome to QuickBizz!!!!"
                from_email=settings.EMAIL_HOST_USER
                to_list=[user.email,settings.EMAIL_HOST_USER]
                send_mail(subject,'please click on following link to verify your email address: http://'+settings.HOST+'/app1/login_firsttime/?uid=%s'%(hash1),from_email,to_list,fail_silently=True)
                messages.success(request, ' verification link has been sent to your email address')
                return render(request,'app1/email.html')
                       
            else:
                
                return render(request,"app1/register.html",{'form':form})
        else:
            form = SignupForm()
            
        return render(request, 'app1/register.html', {
            'form': form
            })

def login_firsttime(request):

    hash1=request.GET.get('uid', '')
    if (hash1):
        email_obj=emailverify.objects.get(activation_key=hash1)
    else:
        raise ValueError('Wrong hashkey')
    time_date=email_obj.registration_time        
    
    if time_date < (datetime.now() - timedelta(hours=24)):
        raise ValidationError('Verification link has been expired')

    form = LoginForm()
    username=User.objects.get(id=email_obj.username.id)
    username.is_active=True
    username.save()
    messages.success(request, "you have verified your email")
    return render(request,"app1/login.html",{'form':form})

def dashboard(request):
    return render(request,"app1/dashboard.html",{})


def products(request):
    return render(request,"app1/products.html",{})

def create_product(request):
    form=ProductForm()
    return render(request,"app1/create_product.html",{'form':form})

