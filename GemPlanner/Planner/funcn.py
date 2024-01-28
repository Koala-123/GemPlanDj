import pathlib
import textwrap
import datetime


import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
#from Planner.models import *
import requests
from vertexai.preview.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

gemPlan1=dict()

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
Based on the below prompt, identify which gemplan(aka task or event) from the given dictionary:-
{prompt}

The dictionary is {gemPlan1}
'''
    task=model.generate_content(GQ).text
    for i in gemPlan1:
        if i in task:
            return i

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
    
    '''gemPlan1.create(name=details[0],date=convertDateTime(details[1]),is_completed=False)
    gemPlan1.save()'''

    gemPlan1[details[0]]=[convertDateTime(details[1]),False]


def editTask(prompt):
    reT=identifyGemplan(prompt)
    Try=f'''
For the given below prompt, and identify the changes in time required to be made.:-
"{prompt}. The identified task is {reT}"
    '''
    response=model.generate_content(Try)
    newTime=response.text

    #details=list(Dict.values())
    
    gemPlan1[reT]=[convertDateTime(newTime,False)]

def removeGemplan(prompt):
    task = identifyGemplan(prompt)
    del gemPlan1[task]

def markGemplan(prompt):
    task = identifyGemplan(prompt)
    gemPlan1[task][1] = True
'''
def viewAll():
    for i in gemPlan1:
        print(f'Gemplan: {i} Date: {gemPlan1[i][0]} Completed: {gemPlan1[i][0]}')

def viewCompleted():
    for i in gemPlan1:
        if gemPlan1[i][1]:
            print(f'Gemplan: {i} Date: {gemPlan1[i][0]} Completed: {gemPlan1[i][0]}')

def viewPending():
    for i in gemPlan1:
        if not gemPlan1[i][1]:
            print(f'Gemplan: {i} Date: {gemPlan1[i][0]} Completed: {gemPlan1[i][0]}')
'''
def generalQuery(prompt):
    model.generate_content(prompt)