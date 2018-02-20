# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = " This is my users page."
	return HttpResponse(response)
def register(request):
	response = "Create a new user record."
	return HttpResponse(response)
def login(request):
	response = "Login Page."
	return HttpResponse(response)
def new(request):
	response = "Redirect to register."
	return redirect('/users/register')
def users(request):
	response = "Display all users"
	return HttpResponse(response)