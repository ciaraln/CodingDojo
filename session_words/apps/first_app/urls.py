from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index), # $ the dollar needs to be in index, just default putting the sign.
  url(r'^session_words$', views.session_words), 
  url(r'^clear$', views.clear), 
]