from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField("auth.User")
    #date_of_birth = models.DateField(null=True)
    bio = models.TextField()


class OrgModel(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField(blank=True, null=True, max_length=240)
    user = models.ForeignKey("Profile")

    class Meta:
        ordering = ['title']


class Header(models.Model):
    title = models.CharField(max_length=240)
    level = models.IntegerField()
    parent = models.ForeignKey('OrgModel')