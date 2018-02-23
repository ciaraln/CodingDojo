from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import Registration
import re
import bcrypt
from django.contrib import messages
emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
nameregex = re.compile(r'^[a-zA-Z]+$')

def index(request):
	return render(request, 'login_app/index.html')


def register(request):
	errors = Registration.objects.basic_validator(request.POST)
	if len(errors): 
		print "Hi"
		for error in errors:
			messages.error(request, error)

		return redirect('/')
	else:
		user = Registration.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		request.session['user_id'] = Registration.objects.get(id=user.id).id
		# register.last_name = request.POST['last_name']
		# register.email_address = request.POST['email_address']
		# register.password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		# register.save()
		logged_in_user = Registration.objects.get(id=request.session['user_id'])
		request.session['logged_in_user'] = logged_in_user.first_name
		request.session['message'] = 'You have successfully registered!'
		print request.session['user']

		return redirect('/reg_success')

def reg_success(request):
	# user = Registration.objects.last()
	# request.session['name'] = user.first_name
	# request.session['id'] = user.id
	return render(request, 'login_app/logsuccess.html')
def login(request):
	if len(errors):
		for error in errors:
			messages.error(request, error)
		return redirect('/')
	else:
		user = Registration.objects.filter(email_address=request.POST['email_address'])
		request.session['user_id'] = user.id
		request.session['message'] = 'You have successfully logged in!'
		return redirect('/reg_success')