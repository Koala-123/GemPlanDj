import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Used to securely store your API key
#from google.colab import userdata


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyAlbo3wlPw0oltmVpM9dEjU-3JFLXZfwnI'

genai.configure(api_key=GOOGLE_API_KEY)
'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
'''

model = genai.GenerativeModel('gemini-pro')
inPrompt=input('Enter what you want to do: ')
#%%time
def fnidentificn(inPrompt):
  prompt=f"""Given the below prompt, Identify if-
  1. The user wants to add a gemplan
  2. The user wants to edit a gemplan
  3. The user wants to remove a gemplan
  4. The user wants to mark a gemplan as completed
  5. The user wants to view gemplans
  6. The user wants to view completed gemplans
  7. The user wants to view pending gemplans
  8. The user is asking a general query: General queries include whether the user is asking to view pending tasks, About reminders or to mark gemplans as done
  9. None of the above

  Assume gemplans is another term for Tasks or events

  The prompt is:-
  {inPrompt}

  """
  try:
    response = model.generate_content(prompt)
    fn=int(response.text[0])
    return fn
  except Exception:
    return 9


#print(to_markdown(response.text))
#print(response.prompt_feedback)
#print(response.candidates)

'''
try:
  print(response.text[0])
  function=int(response.text[0])
except Exception:
  print('Sorry, Gemini was unable to process it.')
  function=9'''