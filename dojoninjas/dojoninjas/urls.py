from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.dojo_ninja.urls')),
    url(r'^admin/', admin.site.urls),
]
