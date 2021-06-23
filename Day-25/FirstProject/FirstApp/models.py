from django.db import models

# Create your models here.

class Register(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)

	# def __str__(self):
	# 	return str(self.id)+" "+self.name

class SignUp(models.Model):
	fname = models.CharField(max_length=50)
	age = models.IntegerField()

	class Meta:
		db_table = 'signup'




