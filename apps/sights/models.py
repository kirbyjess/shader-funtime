from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
  title = models.CharField(max_length = 50)
  abbreviation = models.CharField(max_length = 10)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)


class City(models.Model):
  country = models.ForeignKey(Country, on_delete = models.CASCADE)
  title = models.CharField(max_length = 50)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)


class Sight(models.Model):
  city = models.ForeignKey(City, on_delete = models.CASCADE)
  title = models.CharField(max_length = 200)
  timeEst = models.DecimalField(default = 0, decimal_places = 2, max_digits = 5)
  sightType = models.CharField(max_length = 1, choices = settings.SIGHTCHOICE)
  public = models.BooleanField(default = True)
  created_by = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('sightType', 'title')



