from django.test import TestCase
import unittest 
import os
import string

class Testpass(unittest.TestCase):
	# check both password should be same
	def test_pass1_pass2(self):		
		pass1=os.environ.get('pass1')			
		pass2=os.environ.get('pass2')		
		self.assertEqual(pass1,pass2)
	# check both password should not be same
	def test_pass3_pass4(self):		
		pass1=os.environ.get('pass3')			
		pass2=os.environ.get('pass4')		
		self.assertNotEqual(pass3,pass4)
	# check string have at least 2 character
	def test_string(self):			
		stri = os.environ.get('string')				
		if len(stri)<2:				
			self.assertFalse()			
		else:				
			self.assertTrue()
	# check password lenght should be less than 20 greater than 8
	def test_pass_lenght(self):		
		pass5 =os.environ.get('pass5')
		self.assertFalse(len(pass5)<8 or len(pass5)>20)			
		self.assertTrue(len(pass5)>=8 or len(pass5)<=20)
	def test_username(self):			
		name = os.environ.get('user')		
		for c in name:			
			if c in string.punctuation:				
				self.assertFalse			
			else:				
				self.assertTrue	
	def test_username1(self):			
		uname = os.environ.get('user_name')		
		for c in uname:			
			if c in string.punctuation:				
				self.assertFalse			
			else:				
				self.assertTrue
	