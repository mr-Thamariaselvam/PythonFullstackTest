from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def get_tasks(request):
  result = models.Tasks().objects.get()
  print(result);
  return result;