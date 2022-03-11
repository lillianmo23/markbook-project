import json
from masteryChecks import *
from os import system

# Load json files
with open("mastery-checks.json", "r") as f:
    mastery_checks = json.loads(f.read())
with open("student-checks.json", "r") as f:
    student_checks = json.loads(f.read())

def view_grades():
    """Display a table of all student's grades
    
    Include a menu at the bottom to add grades, edit grades, or go back
    """
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
        
        print(
            "[1] Add a new mastery check\n[2] Edit a mastery check\n[3] Delete a mastery check\n[4] Update Student\n[B]ack"
        )
        choice = input("> ")
        if choice == "1":
            mastery_checks = add_mastery_check(mastery_checks)
        elif choice == "2":
            mastery_checks = edit_mastery_check(mastery_checks)
        elif choice == "3":
            mastery_checks, student_checks = del_checks(mastery_checks, student_checks)
        elif choice == "4":
            student_checks = move_a_student(student_checks)
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
        print("Would you like to...\n[1] View Grades\n[2] View Mastery Checks\n\n[Q]uit")
        choice = input("> ")
        if choice == "1":
            view_grades()
        elif choice == "2":
            view_checks()
        elif choice.lower() == "q":
            return
        else:
            input("Invalid Input.\nPress ENTER to continue.")

if __name__ == "__main__":
    main()
# Update json files
with open("student-checks.json", "w") as f:
    json.dump(student_checks, f, indent = 4)
with open("mastery-checks.json", "w") as f:
    json.dump(mastery_checks, f, indent = 4)
