# function
# classes

# modules
from utilities import sum

# i = sum(2, 4)
# print(i)



# exceptions
try: # here comes code that fails
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError: # what to do if this error occurs
    print("enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")



# lists
# objs (dictionaries)


# type hints (indicate what type of value to expect in return)
def add(a: int, b: int) -> int:
    return a + b



# virtual environments
# (keeps project's py packages separate from other projects)
# create one in your proj folder: python -m venv .venv

# activate the venv
# linux + mac: source .venv/bin/activate
# windows: .venv\Scripts\activate.bat

# when you are done deactivate it with: deactivate 



# pip (python's package installer) -- used to install external libraries
# to save installed packages to a file: python -m pip freeze > requirements.txt
# to install everything from that file: python -m pip install -r requirements.txt



# env variables jo env file me hote
# import os

# app_name = os.getenv("APP_NAME", "DefaultApp")
# print(app_name)



# python's json module converts between json and py data structures
import json
user = { 'name': 'Huzaifa', 'age': 19 }

data = json.dumps(user) # obj to json string
# print(data)

result = json.loads(data) # json string to obj
# print(result)

# json.dump() and json.load() — write and read JSON files.
with open("data.json", "w") as f:
    json.dump({"name": "ALI"}, f)

with open("data.json", "r") as f:
    data2 = json.load(f)
# print(data2)




# HTTP Basics
# get (to retrieve), put (to update/replace), post (to send), delete (to del)

# import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users/1",
#     timeout=10
# )

# response.raise_for_status()

# user = response.json()
# print(user["name"])

# to install: python -m pip install requests