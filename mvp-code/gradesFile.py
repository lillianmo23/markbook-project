def update_grades(grades: dict) -> dict: # Owen
    """Updates student's grades
    
    Args:
        grades: A dictionry of students and their grades
    
    Returns:
        Updated dictionary grades
    """
    try:
        num = int(input("How many grades would you like to update?\n> "))
    except:
        num = 0
        input("Invalid Input.\nPress ENTER to continue.")
    for i in range(num):
        names = input(f"What is student {i+1}'s name?\n> ")
        mark = int(input(f"What is {names}'s average?\n> "))
        grades[names] = mark
    return grades
