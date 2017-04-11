import unittest
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from captcha.models import CaptchaStore
class SimpleTest(TestCase):
	
	def test_login1(self):
		setup_test_environment()
		user = User.objects.create_user(username='vidyahulwan95@gmail.com', email='vidyahulwan95@gmail.com', password='Aasdfg123!')
		user.save()
		c = Client()
		response = c.post(reverse('login_view'), {'username': 'vidyahulwan95@gmail.com', 'password': 'Aasdfg123!'})
		print response
		self.assertRedirects(response, '/app1/dashboard/')
	
	# def test_login2(self):
	# 	setup_test_environment()
	# 	user = User.objects.create_user(username='vidyahulwan95@gmail.com', email='vidyahulwan95@gmail.com', password='Aasdfg123!')
	# 	user.save()
	# 	c = Client()
	# 	response = c.post(reverse('login_view'), {'username': 'vidya@gmail.com', 'password': 'Aasdfg123!'})
	# 	print response
	# 	self.assertRedirects(response, '/app1/login_view/')
	
		
	# def test_register1(self):
	# 	setup_test_environment()
	# 	c = Client()
	# 	captcha = CaptchaStore.objects.all()
	# 	registration_data = { 
	# 							'captcha_0': 'XXXX',
	# 							'captcha_1': 'XXXX'}
	# 	print captcha
	# 	print registration_data 		
	# 	response = c.post(reverse('register'), {' first_name':'vidya','last_name':'hulwan', 'email':'vidyahulwan@gmail.com','email1':'vidyahulwan@gmail.com','password': 'Aasdf123!','password1': 'Aasdf123!','captcha':registration_data})
	# 	print response
	# 	self.assertRedirects(response, '/app1/login_view/')

		# captcha_count = CaptchaStore.objects.count()
		# print captcha_count
		# self.failUnlessEqual(captcha_count, 0)
		# xyz=CaptchaStore.objects.create(challenge='xxx', response='xxx')
		# post_data={}
		# post_data['captcha_0'] = 'xxxx'
		# post_data['captcha_1'] = 'xxxx'


	def test_products(self):
		setup_test_environment()
		c = Client()
		response = c.post(reverse('create_product'), {'product_name':'xyz','category':'mobiles','offer':'benefits','product_details':'ffhhg','product_cost':454,'material_details':'sdggfg','quantity':5,'deliver_charges':45.23,'return_allowed':0,'return_within':0})
		print response
		self.assertTrue(response.status_code,200)		
		print response.content

		





















			# message = list(response.context.get('messages'))[0]
  #   	self.assertEqual(message.tags, "success")
  #   	self.assertTrue("success text" in message.message)
		# self.assertEqual(response.status_code, 302)



		# def test_login(self):    		
  #       	c = Client()
  #       	response = c.post(reverse('login_view'), {'username': 'vidyahulwan95@gmail.com', 'password': 'Aasdfg123!'})
  #       	print response
  #       	
        	# self.assertContains(response, 'login successfully.') # case run

# class PollsViewsTestCase(TestCase):
#     def test_index(self):
#         resp = self.client.get('/app1/dashboard/products/')
#         self.assertEqual(resp.status_code, 200)
#         self.assertTrue('products' in resp.context)
        
# class PollsViewsTestCase(TestCase):
#     def test_index(self):
#         resp = self.client.get('/app1/')
#         self.assertEqual(resp.status_code, 200) # ok

# class PollsViewsTestCase(TestCase):
#     def test_index(self):
#         resp = self.client.get('/register/')
#         self.assertEqual(resp.status_code, 404) #source not found

# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         self.assertEqual(1 + 2, 2)



# import unittest
# import os

# from django.test import TestCase,Client
# from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
# from django.test import RequestFactory

# from . import views
# from .forms import SignupForm,LoginForm

# # Create your tests here.
# """
# def setUp(self):

#     self.user = UserFactory()
#     self.factory = RequestFactory()

# """
# class Test1(unittest.TestCase):
	

# 	def test_valid_form(self):
# 		data = {'email':'vidyahulwan123@gmail.com','email1':'vidyahulwan123@gmail.com','password': 'Aasdf123!','password1':'Aasdf123'}
# 		form = SignupForm(data=data)
# 		self.assertTrue(form.is_valid())

# 	def test_invalid_form(self):
# 		w =User.objects.create(username='vidyahulwan', password='')
# 		data = {'email': w.username, 'password': w.password,}
# 		form = SignupForm(data=data)
# 		self.assertFalse(form.is_valid())
	
# 	def test_valid_login_form(self):
# 		data={'username':'vidyahulwan123@gmail.com','password':'Aasdf123!'}
# 		form=LoginForm(data=data)
# 		self.assertTrue(form.is_valid())
# 	