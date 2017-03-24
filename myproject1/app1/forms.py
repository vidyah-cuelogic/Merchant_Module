
from django import forms 
from captcha.fields import CaptchaField
from django.contrib.auth import (get_user_model,authenticate,login,logout,)

User=get_user_model()

class ContactForm(forms.Form):
    
    email = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'size':'30','placeholder': 'Enter Email address'}))
    email1 = forms.EmailField(label='Confirm Email Address',widget=forms.TextInput(attrs={'size':'30','placeholder': 'Re-enter Email address'}))
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'size':'30','placeholder': 'Enter first name'}))
    last_name=forms.CharField(label='Last name',widget=forms.TextInput(attrs={'size':'30','placeholder': 'Enter last name'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'size':'30','placeholder': 'Enter Password'}))
    password1 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'size':'30','placeholder': 'Re-enter Password'}))
    captcha = CaptchaField()
    
    def clean(self):
        super(ContactForm, self).clean()
        first_name= self.cleaned_data.get('first_name')
        last_name= self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        email1 = self.cleaned_data.get('email1')
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password1')
        
            
        if User.objects.filter(email=email).exists():            
            raise forms.ValidationError("email already exists")
        return self.cleaned_data

class LoginForm(forms.Form):

    username = forms.EmailField(label='Username',widget=forms.TextInput(attrs={'size':'30','placeholder': 'Enter Email address'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'size':'30','placeholder': 'Enter Password'}))
    
    def clean(self):
        super(LoginForm, self).clean()
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("Invalid user")
        return self.cleaned_data
         