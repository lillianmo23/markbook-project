from unicodedata import name

import json

with open("students.json", "r") as f:
    grades = json.loads(f.read())

num_of_students = int(input("how many students would you like to add?"))


for i in range(num_of_students):
    names = input(f"What is student {i+1}'s name?")
    # grades[names] = None


    mark = int(input(f"What is {names}'s average?"))
    print()
    
    grades[names] = mark




print(grades)

with open("students.json", "w") as f:
    json.dump(grades, f, indent = 4) 
