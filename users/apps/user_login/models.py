# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "first_name: {}, last_name: {}".format(self.first_name, self.last_name)

#from apps.user_login.models
#Users.objects.all()
#Users.objects.first()
#Users.objects.last()
#Users.objects.order_by('-last-name')
#Users.objects.create(first_name='joyce', last_name= 'schuster', email='js@js.org',age='27',created_at='now()',updated_at='now()')
# uppercase takes priority over lowercase for order. 
#get and edit/update values below
#u=Users.objects.get(id=3)
#u.last_name='smith'
#u.save()
#Users.objects.get(id=3) to check edit/update
#To delete 
#Users.objects.get(id=4)
#u=Users.objects.get(id=4)
#u.delete()
#u.save()
#u=Users.objects.get(id=4) print DoesNotExist: Users matching query does not exist.
