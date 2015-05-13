from django.db import models

class Upload(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to='repository')
	def __str__(self): 
		return self.title
		
class Upload_0(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to='cat')
	def __str__(self): 
		return self.title

class Upload_1(models.Model):
	title = models.CharField(max_length=50)
	file = models.FileField(upload_to='dog')
	def __str__(self): 
		return self.title
		
class Car(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	photo = models.ImageField(upload_to='cars')