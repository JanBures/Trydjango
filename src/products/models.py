from django.db import models
#from django.utils import timezone
# Create your models here.

class Product(models.Model):
	title 		= models.CharField(max_length=40)
	description = models.TextField(blank=True, null=True)
	priceCZK	= models.DecimalField(decimal_places=2,max_digits=100, default=0.00)
	priceEUR	= models.DecimalField(decimal_places=2,max_digits=100, default=0.00)
	summary		= models.TextField() 
#	vProdejiOd	= models.TimeField(default=timezone.now)

