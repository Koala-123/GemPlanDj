from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'Planner/home.html',{})

def gchat(request):
    return render(request,'Planner/my_gemplanner.html',{})

def gemplans(request):
    return render(request, 'Planner/gemplanList.html',{})