# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = " This is my surveys page."
	return HttpResponse(response)
def create(request):
	response = "Redirect to survey page"
	return redirect('/')
def new(request):
	response = "Add a new survey"
	return HttpResponse(response)
