from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your blog request!"
    return HttpResponse(response)
def new(request):
	response = "Is this blog working."
	return HttpResponse(response)
def create(request):
	response = "Redirect to homepage."
	return redirect('/')

def show(request, num='15'):
	response = "Show 15"
	return HttpResponse(response)

def edit(request, num='11'):
	response = "Edit Page {}".format(num)
	return HttpResponse(response)

def destroy(request, num='16'):
	response = "Destroy Page"
	return redirect('/')