from django.db import models
from jsonfield import JSONField
#from django.contrib.auth.models import User


#class User(models.Model):
#    user = models.OneToOneField(User)
#
#    def __unicode__(self):
#        return self.user.username


class Api(models.Model):
    name = models.CharField(max_length=128, default="trello")
    calls = JSONField(default={})

    def __unicode__(self):
        return self.name


class ApiCredential(models.Model):
    name = models.CharField(max_length=128)
    settings = JSONField(default={})
    api = models.ForeignKey(Api)

   # def __unicode__(self):
    #    return self.name, self.settings


class Call(models.Model):
    api = models.ForeignKey(Api)
    name = models.CharField(max_length=128)
    response = JSONField(default={})

    def __unicode__(self):
        return self.name
