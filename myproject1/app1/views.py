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
                return HttpResponseRedirect('/app1/login/')              
            else:
                return render(request,"app1/register.html",{'form':form})
        else:
            form = ContactForm()
            
        return render(request, 'app1/register.html', {
            'form': form
            })