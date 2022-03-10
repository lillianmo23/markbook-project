from unicodedata import name


import json

def addmasterycheck():
    global check_name
    check_name = input("What is this mastery check called?")
    return check_name

addmasterycheck()

with open("students.json", "a") as f:
    json.dump(check_name, f)
