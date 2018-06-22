from django.shortcuts import render, HttpResponse, redirect
from apps.demo2.models import *
from django.core import serializers
import random
import json
# Create your views here.
def index(request):
    return render(request, 'demo2/index.html')
    # return HttpResponse("hello world")
def search(request):
    return render(request, 'demo2/list.html', {"users" : Users.objects.filter(first_name__startswith=request.POST['type_box'])})