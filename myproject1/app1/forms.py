
from django import forms 
from captcha.fields import CaptchaField
from django.contrib.auth import (get_user_model,authenticate,login,logout)
User=get_user_model()
class ContactForm(forms.Form):   
    email = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'placeholder': 'Enter Email address'}))
    email1 = forms.EmailField(label='Confirm Email Address',widget=forms.TextInput(attrs={'placeholder': 'Re-enter Email address'}))
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name=forms.CharField(label='Last name',widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password1 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))
    captcha = CaptchaField()    
    def clean(self):
        super(ContactForm, self).clean()
        email = self.cleaned_data.get('email')   
                   
        if User.objects.filter(email=email).exists():            
            raise forms.ValidationError("email already exists")
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.EmailField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Enter Email address'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    
    def clean(self):
        super(LoginForm, self).clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if not user:
            print("yes")
            raise forms.ValidationError("Invalid user")
        else:
            print("no")
        return self.cleaned_data
         