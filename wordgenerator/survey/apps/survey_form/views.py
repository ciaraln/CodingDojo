from django.shortcuts import render, redirect
def index(request):
#	print "This is index"
#	request.session.flush() # this will clear all sessions, please do every now and then. 
	if not 'count' in request.session:	
		print 'This is after if statement starts.'
		request.session['count'] = 0 
		request.session['yourfullname'] = ' ' 
		request.session['DojoLocation'] = ' ' 
		request.session['FavoriteLanguage'] = ' '  
		request.session['comment'] = ' '  
	return render(request,'survey_form/index.html')

def processTest(request):
	request.session['count'] += 1
	request.session['yourfullname'] = request.POST['yourfullname']
	request.session['DojoLocation'] = request.POST['DojoLocation']
	request.session['FavoriteLanguage'] = request.POST['FavoriteLanguage']
	request.session['comment'] = request.POST['comment']
	return redirect('/viewResult')

def viewResult(request):
	return render(request,'survey_form/result.html')
