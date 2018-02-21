# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "I am working."
	return HttpResponse(response)

def__str__(self):
	return "first_name: {}, last_name: {}".format(self.first_name, self.last_name)

# Create your views here.
