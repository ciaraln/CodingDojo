# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	desc = models.TextField()

class ninjas(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojos =  models.ForeignKey(dojos, related_name="ninjas")

#dojos.objects.first().ninjas.all().values() to pull up all ninjas to first city
#dojos.objects.first().ninjas.all().values() tp pull up all ninjas from last city