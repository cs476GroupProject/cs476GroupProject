from django.db import models

# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    preference = models.CharField(max_length=255, blank=True, null=True)





class Customized(models.Model):
    cid = models.AutoField(primary_key=True)
    url = models.CharField(db_column='URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    imgname = models.CharField(max_length=2000, blank=True, null=True)
    sitename = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='app01/static/img/webimg/', null=True)
    uid = models.ForeignKey(Users, models.DO_NOTHING, db_column='uid', blank=True, null=True)



class Website(models.Model):
    wid = models.AutoField(primary_key=True)
    url = models.CharField(db_column='URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=2000, blank=True, null=True)



