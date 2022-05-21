from _adduser import adduser
from detection import isPresent
import sys
import csv
from datetime import date
import pandas as pd
# import numpy as np

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
        print("Adding student ...")
        data = [0] * 12
        data[0] = rollno
        with open('data.csv', 'a') as csvfile:
            csvwrite = csv.writer(csvfile)
            csvwrite.writerow(data)
        print(f"Student with roll number {rollno} added successfully")
        return

def markattendance():
    current_timings = date.today()
    today = f'{current_timings.day}-{current_timings.month}'
    print(today)
    print("Enter the roll number")
    while True:
        try:
            rollno = int(input(">> "))
            break
        except ValueError:
            print("Please Enter valid roll number")
    ret = isPresent(str(rollno))
    if ret == -1:
        print("The rollno is not in database. Please add the rollno first using option 2")
        return
    elif ret == 0:
        print("Not able to open camera. Try again")
        return
    elif ret == 1:
        df = pd.read_csv("data.csv")
        index = df[df['roll_no'] == rollno].index[0]
        df.at[index, today] = 1
        # df.set_value(index, today, 1)
        df.to_csv("data.csv", index=False)
        # df.loc(df['roll_no'] == rollno, today) = 1
        print(f'Attendance marked for rollno {rollno}')
        return

def main():
    print(initial)
    while True:
        try:
            x = int(input(">> "))
            if x in range(1,4):
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