from unicodedata import name
from typing import List
import json

def add_mastery_check():
    """Adds a new mastery check with a selected name"""
    global check_name
    check_name = input("What is this mastery check called?")
    with open("students.json", "a") as f:
        json.dump(check_name, f)

def del_checks(mastery_checks: List[str], student_checks: dict) -> List[str]:
    """Removes a mastery check from the list of checks, and moves students to their new mastery check
    
    Args:
        mastery_checks: The list of mastery checks
        student_checks: The list of checks students are on
    
    Returns:
        An updated list with the chosen check removed
        An updated dictionary of student information
    """
    while True:
        print("What mastery check would you like to delete?")
        choice = input("> ")
        index = mastery_checks.index(choice)
        mastery_checks.remove(choice)
        for key, value in student_checks.items():
            if value > index + 1:
                student_checks[key] = value - 1
        break
    return mastery_checks, student_checks
