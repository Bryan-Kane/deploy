from django.shortcuts import render, HttpResponse, redirect
from apps.demo1.models import *
from django.core import serializers
import random
import json
# Create your views here.
def index(request):
    return render(request, 'demo1/index.html')
    # return HttpResponse("hello world")

def jsn(request):
    users = Users.objects.all()
    return HttpResponse(serializers.serialize("json", users), content_type ='application/json')


def htl(request):
    return render(request, 'demo1/jsn.html', {'jsn':Users.objects.all()})