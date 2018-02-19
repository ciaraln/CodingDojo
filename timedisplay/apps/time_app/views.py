from __future__ import unicode_literals
from django.shortcuts import render 
from datetime import datetime

def index(request):
	now = datetime.today()
	context = {
	"date": now.strftime("%b %d, %Y"), # lower case letters in html and views.py
	"time": now.strftime("%I:%M %p"), # lower case letters in html and views.py
	}
	return render(request,'time_app/index.html', context)
