import pathlib
import textwrap
import datetime


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from Planner.models import *
import requests
from vertexai.preview.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

gemPlan1=GemPlans(name="GemPlans")

GOOGLE_API_KEY='AIzaSyAlbo3wlPw0oltmVpM9dEjU-3JFLXZfwnI'

model = genai.GenerativeModel('gemini-pro')


'''identifyGemplan=FunctionDeclaration(
    name="Identify Task",
    description="Identifies the task from the database",
    parameters={
        "type":"object",

    }
)'''

def identifyGemplan(prompt):
    GQ=f'''
Based on the below prompt, identify which gemplan(aka task or event) is being mentioned:-
{prompt}
'''
    task=model.generate_content(GQ).text
    return task

def convertDateTime(x):
    time=datetime.datetime.strptime(x,'%d %b %Y %I:%M%p')
    return time

def addTask(prompt):
    Try=f'''
In the below prompt, extract the task/event, date and time and when to be reminded to a dictionary in python: -
"{prompt}"
'''
    response=model.generate_content(Try)
    Dict=eval(response.text[(response.text).find('{'):(response.text).find('}')+1])

    details=list(Dict.values())
    
    gemPlan1.create(name=details[0],date=convertDateTime(details[1]),is_completed=False)
    gemPlan1.save()


def editTask(prompt):
    Try=f'''
For the given below prompt, Identify the task mentioned (or gemplan. Assume gemplan is another term for task or event) and identify the changes needed to be made:-
"{prompt}"
    '''
    ...

def removeTask(prompt):
    ...