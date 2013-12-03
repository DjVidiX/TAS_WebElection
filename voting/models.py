from django.db import models


class Partia(models.Model):
    nazwa = models.CharField(max_length=30)
    skrot = models.CharField(max_length=5)

    def __unicode__(self):
        return self.nazwa


class Kandydat(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    partia = models.ForeignKey(Partia)
    haslo_wyborcze = models.TextField()
    wiek = models.IntegerField()
    zdjecie = models.ImageField(upload_to='static/candidates')

    def __unicode__(self):
        return self.imie + " " + self.nazwisko


class Obywatel(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    PESEL = models.CharField(max_length=11)
    nr_dowodu = models.CharField(max_length=9)

    def __unicode__(self):
        return self.imie + " " + self.nazwisko


class Glos(models.Model):
    kandydat = models.ForeignKey(Kandydat)

    def __unicode__(self):
        return self.kandydat



# Create your models here.
