from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Information(models.Model):
	name = models.CharField(max_length=100, blank=False, default='Enter Full Name here')
	email = models.EmailField(blank=False,default='Enter Email here')
	mobile = models.CharField(max_length=10, blank=False,default='Enter Mobile Number here')
	info= models.CharField(max_length=300,blank=False,default='Enter Description about book ')
	cost=models.CharField(max_length=4,blank=False,default='Enter Cost of the book ')

	def __str__(self):
		return self.name
