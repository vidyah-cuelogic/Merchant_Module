
from django import forms 
from captcha.fields import CaptchaField
from django.contrib.auth import (get_user_model)
from app1.models import Products
User=get_user_model()
YESNO_CHOICES = ((0, 'No'), (1, 'Yes'))

class SignupForm(forms.Form):    
    email = forms.EmailField(label='Email Address',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Email address','title':'plz vidya'}))
    email1 = forms.EmailField(label='Confirm Email Address',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Re-enter Email address'}))
    first_name = forms.CharField(label='First name',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter first name'}))
    last_name=forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter last name'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter Password'}))
    password1 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Re-enter Password'}))
    captcha = CaptchaField()
    
    def clean(self):
        super(SignupForm, self).clean()
        email = self.cleaned_data.get('email') 
        if User.objects.filter(email=email).exists():            
            raise forms.ValidationError("email already exists")
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.EmailField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Email address'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter Password'}))

class ProductForm(forms.Form):
    product_name=forms.CharField(label='Product Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    category=forms.CharField(label='Category',widget=forms.TextInput(attrs={'class':'form-control'}))
    offer=forms.CharField(required=False,label='Offer',widget=forms.TextInput(attrs={'class':'form-control'}))
    product_details=forms.CharField(label='Product Details',widget=forms.Textarea(attrs={'rows':4,'class':'form-control'}))
    product_cost=forms.DecimalField(label='Product cost',widget=forms.TextInput(attrs={'class':'form-control'}))
    material_details=forms.CharField(label='Material Details',widget=forms.Textarea(attrs={'rows':4,'class':'form-control'}))
    quantity=forms.IntegerField(label='Quantity',widget=forms.NumberInput(attrs={'class':'form-control','min':0}))
    deliver_charges=forms.DecimalField(label='Delivery Charges',widget=forms.TextInput(attrs={'class':'form-control'}))
    return_allowed = forms.TypedChoiceField(
                     choices=YESNO_CHOICES, widget=forms.RadioSelect, coerce=int
                )
    return_within=forms.CharField(required=False,label='Return Within',widget=forms.NumberInput(attrs={'class':'form-control','min':0}))
    