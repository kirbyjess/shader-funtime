from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Trek(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  sights = models.ManyToManyField('sights.Sight')
  title = models.CharField(max_length = 200)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)


class Itinerary(models.Model):
  trek = models.ForeignKey(Trek, on_delete = models.CASCADE)
  title = models.CharField(max_length = 200)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)


class ItineraryDate(models.Model):
  itinerary = models.ForeignKey(Itinerary, on_delete = models.CASCADE)
  itineraryDay = models.DateField
  flexible = models.BooleanField(default = True)
  note = models.TextField
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.itineraryDay

  class Meta:
    ordering = ('created_at',)


class Route(models.Model):
  itinerary = models.ForeignKey(Itinerary, on_delete = models.CASCADE)
  title = models.CharField(max_length = 200)
  coordinates = models.CharField
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)
