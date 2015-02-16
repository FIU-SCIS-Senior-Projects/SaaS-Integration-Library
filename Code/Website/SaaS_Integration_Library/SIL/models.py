from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Api_Credential(models.Model):
    name = models.CharField(max_length=128)
    settings = JSONField(default={})

    #def __unicode__(self):
        #return self.name, self.settings
