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
from app1.forms import ContactForm,LoginForm
from django.contrib.auth.models import User

def home(request):
    return render(request,"app1/dashboard.html",{})

    
def login(request):
    if request.method == 'GET':
            form = LoginForm()
            return render(request,"app1/login.html",{'form':form})
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

                return render(request,"app1/dashboard.html")
        else:  
                return render(request,"app1/login.html",{'form':form})
    

def register(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            
            if form.is_valid()  :
                user = User.objects.create_user(form.cleaned_data['email'],form.cleaned_data['email'], form.cleaned_data['password']) 
                user.first_name=form.cleaned_data['first_name']
                user.last_name=form.cleaned_data['last_name']
                user.is_active=False
                      
                user.save() 
                hash1 = str(uuid.uuid1()) 
                e1=user.emailverify_set.create(activation_key=hash1)
                subject="Welcome Successful Registered!!!!"
                from_email=settings.EMAIL_HOST_USER
                to_list=[user.email,settings.EMAIL_HOST_USER]
                send_mail(subject,'please click the given link to log in: http://127.0.0.1:8002/app1/login_firsttime/?uid=%s'%(hash1),from_email,to_list,fail_silently=True)
                messages.success(request, ' email verification link has been sent to registered mail')
                return render(request,'app1/email.html')
                # return HttpResponseRedirect('/app1/login/')              
            else:
                
                return render(request,"app1/register.html",{'form':form})
        else:
            form = ContactForm()
            
        return render(request, 'app1/register.html', {
            'form': form
            })

def login_firsttime(request):

    hash1=request.GET.get('uid', '')
    if (hash1):
        email_obj=emailverify.objects.get(activation_key=hash1)
    else:
        raise ValueError('Wrong hashkey')
    time_date=emailverify_obj.registration_time        
    
    if time_date < (datetime.now() - timedelta(hours=24)):
        raise ValidationError('LinkExpired because link valid for 24 hr only')

    form = LoginForm()
    username=User.objects.get(id=email_obj.username.id)
    username.is_active=True
    username.save()
    messages.success(request, "you have verified your email")
    return render(request,"app1/login.html",{'form':form})

def product(request):
    return render(request,"app1/product.html",{})
