from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
	if 'list' not in request.session:
	 	request.session['list'] = []
	# 	print "hitting list reset"
	return render(request,'index.html')

def session_words(request):
	now = datetime.today()
	if not 'color' in request.POST:
		color = 'black'
	else:
		color = request.POST['color']

	if 'checkbox' in request.POST:
		font = 24
	else: 
		font = 12

	word = {
		'word': request.POST['word'],
		'color': color,
		'font': font,
		'time': now.strftime("%I:%M %p" "%b %d, %Y") # lower case letters in html and views.py
	}
	request.session['listwords'] = request.session['list'].append(word)
	print request.session['list']
	request.session.modifed=True
	return redirect('/', word)

def clear(request):
	request.session.clear()  
	return redirect('/')