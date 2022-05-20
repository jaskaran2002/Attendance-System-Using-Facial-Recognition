from _adduser import adduser
from detection import isPresent
import sys

initial = """
Choose option:
    1. Mark attendance
    2. Add student
    3. Exit
"""

def addinguser():
    print("Enter the roll number of the new user to be added")
    while True:
        try:
            rollno = int(input(">> "))
            break
        except ValueError:
            print("Please Enter valid roll number")
    ret = adduser(rollno)
    if ret == "directory exists":
        print("The student already exists")
        return
    elif ret == 0:
        print("Not able to open camera. Try again")
        return
    else:
        # Add user to csv
        print(f"Student with roll number {rollno} added successfully")
        return

def markattendance():
    pass

def main():
    print(initial)
    while True:
        try:
            x = int(input(">> "))
            if (x == 1) or (x == 2):
                break
            else:
                print("Please Enter option 1 or 2")
            
        except ValueError:
            print("Please Enter option 1 or 2")
    
    if x == 2:
        addinguser()
    elif x == 1:
        markattendance()
    else:
        return 'exit'



if __name__ == "__main__":
    # Opening csv
    while True:
        y = main()
        if y == 'exit':
            # Closing csv
            sys.exit()