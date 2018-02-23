from __future__ import unicode_literals
from django.contrib import messages 
from django.db import models

import re
import bcrypt
emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
nameregex = re.compile(r'^[a-zA-Z]+$')

class RegistrationManager(models.Manager):
	def basic_validator(self,postData):
		errors = []
		if len(postData['first_name']) < 2:
			errors.append('First name must be longer than 1 character')
		if not nameregex.match(postData['first_name']):
			errors.append('First name must be letters only')
		if len(postData['last_name'] ) < 2:
			errors.append('User last name should be more than 2 characters')
		if not nameregex.match(postData['last_name']):
			errors.append('Last name must contain letters only')
		if not emailregex.match(postData['email_address']):
			errors.append('Not a valid E-Mail')
		check = Registration.objects.filter(email_address=postData['email_address'])
		if len(check)>0:
			errors.append('User already exists.')
		if len(postData['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		if postData['password'] != postData['passwordcheck']:
			errors.append('Passwords do not match')
		return errors
		def login_validator(self,postData):
			errors = []
			check = Registration.objects.filter(email_address=postData['email_address'])
			if len(check)<1:
				errors.append('User does not exist.')
			else: 
				if bcrypt.checkpw(postData['password'].encode(),checkpassword.encode() == false):
					errors.append('Invalid Password')
				return errors

class Registration(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)
	objects = RegistrationManager()

# class LoginManager(models.Manager):


# 	def login_validator(self,postData):
# 		errors = []
# 		check = Registration.objects.filter(email_address=postData['email_address'])
# 		if len(check)<1:
# 			errors.append('User does not exist.')
# 		else: 
# 			if bcrypt.checkpw(postData['password'].encode(),checkpassword.encode() == false):
# 				errors.append('Invalid Password')
# 			return errors

class Login(models.Model):
	email_address = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	objects = RegistrationManager()