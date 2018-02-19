from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index), # $ the dollar needs to be in index, just default putting the sign.
  url(r'^processTest', views.processTest),
  url(r'^viewResult', views.viewResult),
]
