import json
from os import system

mastery_checks = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]
with open("student-checks.json", "r") as f:
    student_checks = json.loads(f.read())

def view_grades():
    """Display a table of all student's grades
    
    Include a menu at the bottom to add grades, edit grades, or go back
    """
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
    print("View Grades function")

def view_students():
    while True:
        system("clear")
        print("Print a list of students here")
        print("[1] Add new students\n[B]ack")
        choice = input("> ")
        if choice == "1":
            print() # Add student function
        elif choice == "b":
            return
        else:
            input("Invalid Input.\nPress ENTER to continue.")

def view_checks(): # Jack
    """Display a table of all student's mastery checks
    
    Include a menu at the bottom to add checks, edit checks, or go back
    """
    while True:
        system("clear")
        global mastery_checks, student_checks
        table = "        "
        for check in mastery_checks:
            table += check + " "
        print(table)
        print("="*len(table))
        for key, value in student_checks.items():
            print(key + "\t"*value + "∰")
        print("="*len(table))
        
        print("[1] Add new mastery checks\n[2] Edit mastery checks\n[3] Delete master checks\n[B]ack")
        choice = input("> ")
        if choice == "1":
            print("Handle choice 1") # Create a function to add mastery checks
        elif choice == "2":
            print("Handle choice 2") # Create a function that edits mastery checks
        elif choice == "3":
            print("Handle choice 3") # Create a function that deletes mastery checks
        elif choice.lower() == "b":
            return
        else:
            input("Invalid Input.\nPress ENTER to continue.")

def main(): # Jack
    """Displays a menu upon running the file
    
    Menu will prompt to choose between checking grades and mastery checks
    """
    while True:
        system("clear")
        print("Would you like to...\n[1] View Grades\n[2] View Mastery Checks\n[3] View Student Info\n[Q]uit")
        choice = input("> ")
        if choice == "1":
            view_grades()
        elif choice == "2":
            view_checks()
        elif choice == "3":
            view_students()
        elif choice.lower() == "q":
            return
        else:
            input("Invalid Input.\nPress ENTER to continue.")

if __name__ == "__main__":
    main()
