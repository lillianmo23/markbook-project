def view_grades():
    """Display a table of all student's grades
    
    Include a menu at the bottom to add grades, edit grades, or go back
    """
    print("View Grades function")

def view_checks(): # Jack
    """Display a table of all student's mastery checks
    
    Include a menu at the bottom to add checks, edit checks, or go back
    """
    while True:
        print("Table goes here")
        print("[1] Add new mastery checks\n[2] Edit mastery checks\n[B]ack")
        choice = input("> ")
        if choice == "1":
            print("Handle choice 1") # Create a function to add mastery checks
        elif choice == "2":
            print("Handle choice 2") # Create a function that edits mastery checks
        elif choice.lower() == "b":
            return
        else:
            input("Invalid Input.\nPress ENTER to continue.")

def main(): # Jack
    """Displays a menu upon running the file
    
    Menu will prompt to choose between checking grades and mastery checks
    """
    while True:
        print("Would you like to...\n[1] View Grades\n[2] View Mastery Checks\n[Q]uit")
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
