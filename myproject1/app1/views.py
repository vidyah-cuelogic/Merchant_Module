from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from app1.models import Merchants,emailverify,Products,Categories,Product_Category,Offers,Product_color_images,Merchant_Products
from datetime import datetime, timedelta
import hashlib
import os
import uuid
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from app1.forms import SignupForm,LoginForm,ProductForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request,"app1/home.html",{})

def login_view(request):    
    username = password = ''
    if request.method == 'GET':
            form = LoginForm()
            return render(request,"app1/login.html",{'form':form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/app1/dashboard/')
        else:  
                messages.success(request, ' Invalid user')
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
                form = LoginForm(request.POST)
                return render(request,'app1/login.html',{'form':form})
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
    return HttpResponseRedirect('/app1/login_view/')

@login_required(login_url='/app1/login_view/')
def dashboard(request):
    return render(request,"app1/dashboard.html",{})

@login_required(login_url='/app1/login_view/')
def products(request):
    return render(request,"app1/products.html",{})

@login_required(login_url='/app1/login_view/')
def create_product(request):
    if request.method == 'GET':
        form=ProductForm()
        return render(request,"app1/create_product.html",{'form':form})
    if request.method == 'POST':
        data=request.POST;
        a=Products(product_name=data[u'product_name'],quantity=data[u'quantity'],product_cost=data[u'product_cost'] ,deliver_charges=data[u'deliver_charges'] ,return_allowed=data[u'return_allowed'],return_within=data[u'return_within'],product_speficication=data[u'product_specification'],material_speficication=data[u'material_details'])
        a.save()
        return HttpResponse("data insert into database")            
    return HttpResponse("Something went wrong")
     