from django.db import models


class Sampleinfo(models.Model):
    sampleid = models.CharField(max_length=40, primary_key=True)
    archperiod = models.CharField(max_length=100)
    archculture = models.CharField(max_length=200)
    archdate = models.CharField(max_length=100)
    archsite = models.CharField(max_length=100)
    geopoint = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    long = models.DecimalField(max_digits=8, decimal_places=6)
    geneticsex = models.CharField(max_length=100)
    mtdnahg = models.CharField(max_length=100)
    ychrhg = models.CharField(max_length=100)
    wgsdata = models.CharField(max_length=200)
