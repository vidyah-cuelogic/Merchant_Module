from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from app1.forms import ContactForm,LoginForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,"app1/home.html",{})

    
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
                user.save() 
                form = LoginForm()
                subject="Welcome Account Creation Successful!!!!!"
                from_email=settings.EMAIL_HOST_USER
                to_list=['vidyahulwan95@gmail.com']
                send_mail(subject,'please click the given link to log in: http://172.21.32.80:8000/analysisreport/email_verification/',from_email,to_list,fail_silently=True)
                return HttpResponseRedirect('/app1/login/')              
            else:
                return render(request,"app1/register.html",{'form':form})
        else:
            form = ContactForm()
            
        return render(request, 'app1/register.html', {
            'form': form
            })

def product(request):
    return render(request,"app1/product.html",{})
