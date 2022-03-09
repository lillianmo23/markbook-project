def view_grades():
    """Display a table of all student's grades
    
    Include a menu at the bottom to add grades, edit grades, or go back
    """
    print("View Grades function")

def view_checks(): # Jack
    """Display a table of all student's mastery checks
    
    Include a menu at the bottom to add checks, edit checks, or go back
    """
    print("View Checks function")

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
            print("Invalid Input.")
        input("Press ENTER to continue.")

if __name__ == "__main__":
    main()
