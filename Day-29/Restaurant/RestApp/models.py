from django.db import models

# Create your models here.

class Restaurant(models.Model):
	rname = models.CharField(max_length=30)
	nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	address = models.CharField(max_length=50)