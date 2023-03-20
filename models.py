# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    preference = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Users'



class Customized(models.Model):
    cid = models.AutoField(primary_key=True)
    url = models.CharField(db_column='URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(max_length=50, blank=True, null=True)
    uid = models.ForeignKey(Users, models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'customized'


class News(models.Model):
    nid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=255, blank=True, null=True)
    uid = models.ForeignKey(Users, models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'news'


class Website(models.Model):
    wid = models.AutoField(primary_key=True)
    url = models.CharField(db_column='URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    sitetype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'website'
