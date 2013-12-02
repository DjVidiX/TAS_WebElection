from django.db import models

class Kandydat(models.Model):
	imie = models.CharField(max_length=30)
	nazwisko = models.CharField(max_length=30)
	zdjecie = models.ImageField(upload_to='static/candidates')

	

# Create your models here.
