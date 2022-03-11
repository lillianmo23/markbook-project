def update_grades(grades: dict) -> dict: # Owen
    """Updates student's grades
    
    Args:
        grades: A dictionary of students and their grades
    
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
        mark = input(f"What is {names}'s average?\n> ")
        try:
            grades[names] = int(mark)
        except:
            input("Invalid Input.\nPress ENTER to continue.")
    return grades
