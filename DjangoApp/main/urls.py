from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.first_app.urls')), #no slash for 1st url 
	url(r'^first_app/$', include('apps.first_app.urls')), #slash with the following html urls. 
	url(r'^blogs/', include('apps.blogs.urls')), #include a $ to end the route url.
	url(r'^surveys/', include('apps.surveys.urls')),
	url(r'^users/', include('apps.users.urls')),
] #an array this is the result of the function 