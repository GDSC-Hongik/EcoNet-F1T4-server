from django.db import models
from django.conf import settings


class MapoDistrict(models.Model):
    district = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mapo_district'


class Bin(models.Model):
    category = models.TextField()
    location = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    detail = models.CharField(max_length=100, blank=True, null=True)
    management = models.CharField(max_length=100, blank=True, null=True)
    acceptible = models.CharField(max_length=100)
    unacceptible = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Bin'

class Information(models.Model):
    info_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    bin = models.ForeignKey(Bin, models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Information'

    
class Pictures(models.Model):
    picture_id = models.AutoField(primary_key=True)
    picture = picture = models.ImageField(upload_to='pictures/')
    bin = models.ForeignKey(Bin, models.DO_NOTHING, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, null=False)


    class Meta:
        managed = False
        db_table = 'Pictures'

    
class Information(models.Model):
    info_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    bin = models.ForeignKey(Bin, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Information'