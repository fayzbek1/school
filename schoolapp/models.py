from django.db import models

# Create your models here.

class Kitoblar(models.Model):
    ona_tili = models.TextField()
    jismoniy_tarbiya = models.TextField()
    tasviriy_sanat = models.TextField()
    geografiya = models.TextField()
    informatika = models.TextField()
    kimyo = models.TextField()
    musiqa = models.TextField()
    fizika = models.TextField()
    algebra = models.TextField()
    geometriya = models.TextField()
    biologiya = models.TextField()
    tarix = models.TextField()

class Teachers(models.Model):
    name = models.CharField(max_length=30)
    fulname = models.CharField(max_length=30)
    Tugilgan_yili = models.DateField(max_length=30)
    Lavozimi = models.CharField(max_length=30)
    Maoshi = models.TextField()
    Oquvchisi = models.TextField()
