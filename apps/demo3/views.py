from django.shortcuts import render, HttpResponse, redirect
from apps.demo3.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import random
import json
# Create your views here.

def index(request):
    return render(request, 'demo3/index.html')
@csrf_exempt
def create(request):
    if request.method == 'POST':
        print(request.POST)
        Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], age=request.POST['age'])
        print(request.POST)
        return render(request, 'demo3/repo.html', {'users':Users.objects.all()})
    # return HttpResponse("hello world")
# def search(request):
#     return render(request, 'demo2/list.html', {"users" : Users.objects.filter(first_name__startswith=request.POST['type_box'])})