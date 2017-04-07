import unittest
import os

from django.test import TestCase,Client
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory

from . import views
from .models import Organisation
from .forms import SignupForm,LoginForm

# Create your tests here.
"""
def setUp(self):

    self.user = UserFactory()
    self.factory = RequestFactory()

"""
class Test1(unittest.TestCase):
	

	def test_valid_form(self):
		data = {'email':'vidyahulwan123@gmail.com','email1':'vidyahulwan123@gmail.com','password': 'Aasdf123!','password1':'Aasdf123'}
		form = SignupForm(data=data)
		self.assertTrue(form.is_valid())

	def test_invalid_form(self):
		w =User.objects.create(username='vidyahulwan', password='')
		data = {'email': w.username, 'password': w.password,}
		form = SignupForm(data=data)
		self.assertFalse(form.is_valid())
	
	def test_valid_login_form(self):
		data={'username':'vidyahulwan123@gmail.com','password':'Aasdf123!'}
		form=LoginForm(data=data)
		self.assertTrue(form.is_valid())
	
