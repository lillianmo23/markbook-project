from unicodedata import name
from typing import List
import json

def addmasterycheck():
    global check_name
    check_name = input("What is this mastery check called?")
    return check_name

addmasterycheck()

with open("students.json", "a") as f:
    json.dump(check_name, f)

def del_checks(mastery_checks: List[str]) -> List[str]:
    """Removes a mastery check from the list of checks
    
    Args:
        mastery_checks: The list of mastery checks
    
    Returns:
        An updated list with the chosen check removed
    """
    while True:
        print("What mastery check would you like to delete?")
        choice = input("> ")
        try:
            mastery_checks.remove(choice)
            break
        except:
            input("Invalid Input.\nPress ENTER to continue.")
    return mastery_checks
    
