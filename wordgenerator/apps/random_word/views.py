# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	# request.session['count']=1
	if not 'count' in request.session: # the if not  statement lets me know that there is nothing, so we must initiate the page. 
		request.session['count'] = 1  # define count in here or initiate the page, so we can start at one. 
		print 'count'
		if not 'letters' in request.session:
			request.session['letters'] = '' # you wan to start witn nothing
	return render(request, 'random_word/index.html') #renders request to next method or function

def random_word(request):#this function reeives the request
	request.session['count'] += 1 #the request is aksing for variable to be incremented by 1. 
	request.session['letters'] = get_random_string(length=14)
	return redirect('/')
