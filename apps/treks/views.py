from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Trek

def index(request):
  trek_list = Trek.objects.all()
  template = loader.get_template('treks/index.html')
  context = {
    'trek_list': trek_list,
  }
  return HttpResponse(template.render(context, request))

def detail(request, trek_id):
  try:
    trek = Trek.objects.get(pk = trek_id)
  except Trek.DoesNotExist:
    trek = None
  # trek = get_object_or_404(Trek, pk = trek_id)
  template = loader.get_template('treks/detail.html')
  context = {
    'trek': trek,
  }
  return HttpResponse(template.render(context, request))

def route(request, trek_id):
  try:
    trek = Trek.objects.get(pk = trek_id)
    route = trek.route
  except Trek.DoesNotExist:
    route = None
  # trek = get_object_or_404(Trek, pk = trek_id)
  template = loader.get_template('treks/route.html')
  context = {
    'route': route,
  }
  return HttpResponse(template.render(context, request))
