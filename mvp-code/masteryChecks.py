from typing import List

def add_mastery_check(mastery_checks: List[str]) -> List[str]:
    """Adds a new mastery check
    
    Args:
        mastery_checks: The initial list of mastery checks
    
    Returns:
        Updated mastery_checks with a new mastery check
    """
    check_name = input("What is this mastery check called?\n> ")
    mastery_checks.append(check_name)
    return mastery_checks
    
def move_a_student(student_checks: dict) -> dict:
    """Changes the mastery check a student is on
    
    Args:
        student_checks: Dictionary of checks the students are on
    
    Returns:
        Updated student_checks with edited student information
    """
    student = input("What's the student's name?\n> ")
    check_level = input("\nWhat mastery check are they on right now?\n> ")
    try:
        student_checks[student] = int(check_level)
    except:
        input("Invalid Input.\nPress ENTER to continue.")
    return student_checks

def del_checks(mastery_checks: List[str], student_checks: dict) -> List[str]:
    """Removes a mastery check from the list of checks, and moves students to their new mastery check
    
    Args:
        mastery_checks: The list of mastery checks
        student_checks: The dictionary of checks students are on
    
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

def edit_mastery_check(mastery_checks: List[str]) -> List[str]:
    """Edits a mastery check

    Args:
        mastery_checks: List of mastery checks

    Returns:
        Updated mastery_checks
    """
    edit_index = input("Which mastery check would you like to edit?\n> ")
    edit_to = input("What would you like to change it to?\n> ")
    try:
        mastery_checks[mastery_checks.index(str(edit_index))] = edit_to
    except:
        input("Invalid Input.\nPress ENTER to continue.")
    return mastery_checks
