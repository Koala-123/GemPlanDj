from django.shortcuts import render
from .funcn import *
# Create your views here.

def home(request):
    return render(request,'Planner/home.html',{})

def gchat(request):
    
    
    return render(request,'Planner/my_gemplanner.html',{'gemPlan1':gemPlan1})


def gemplans(request):
    return render(request, 'Planner/gemplanList.html',{'gemPlan1':gemPlan1})