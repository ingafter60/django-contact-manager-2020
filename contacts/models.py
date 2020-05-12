from django.db import models
from django.utils.timezone import datetime

# Contact model
class Contact(models.Model):
	name		= models.CharField(max_length=30)
	email		= models.CharField(max_length=100)
	phone		= models.IntegerField()
	info		= models.CharField(max_length=30)
	gender	= models.CharField(max_length=30, choices=(
							('male', 'Male'),
							('female', 'Female'),
							('other', 'Other')))
	image		= models.ImageField(upload_to='images/', blank=True)
	date_added 	= models.DateTimeField(default=datetime.now)


	def __str__(self):
		return self.name

	