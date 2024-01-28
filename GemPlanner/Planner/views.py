from django.shortcuts import render
from .funcn import *
#from .main import fnidentificn
# Create your views here.

def home(request):
    return render(request,'Planner/gem1.html',{})

def gchat(request):
    inPrompt = request.POST.get('What do you want to do?')
    return render(request,'Planner/GemPlanner.html',{'gemPlan1':gemPlan1,'response':mainStuff(inPrompt)})
 
def gemplans(request):
    return render(request, 'Planner/gemplanList.html',{'gemPlan1':gemPlan1})