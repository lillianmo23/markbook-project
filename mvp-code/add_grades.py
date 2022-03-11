from unicodedata import name

import json

grades = {
    
}
num_of_students = int(input("how many students do you have?"))
for i in range(num_of_students):
    names = input(f"What is student {i+1}'s name?")
    print()
    mark = int(input(f"What is {name}'s average?"))
    print()
    
    grades[name] = mark


with open("students.json", "a") as f:
    json.dump(grades, f)
