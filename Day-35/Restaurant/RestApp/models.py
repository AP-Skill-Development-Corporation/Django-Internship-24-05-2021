from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Restaurant(models.Model):
	rname = models.CharField(max_length=30)
	nitems = models.IntegerField()
	timings = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	rsimg = models.ImageField(upload_to='Restaurantimages/',default='ics.jpg')
	uid = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.rname


class Itemlist(models.Model):
	y = [('NV','Non-Veg'),('VG','Veg'),('Df','Select Item Type')]
	p = [('AV','Available'),('NA','Not Available'),('Sl','Select Availability')]
	iname = models.CharField(max_length=50)
	icategory = models.CharField(choices=y,default="Df",max_length=12) 
	price = models.DecimalField(decimal_places=2,max_digits=8)
	iimage = models.ImageField(upload_to='Itemimages/',default='ics.jpg')
	itavailability = models.CharField(choices=p,default="Sl",max_length=20)
	rsid = models.ForeignKey(Restaurant,on_delete=models.CASCADE)


