import cv2 as cv
import sys
import os


def adduser(rollno):
    try:
        os.mkdir(f"KNOWN_FACES/{rollno}")
    except:
        return "directory exists"

    cap = cv.VideoCapture(0)

    if not(cap.isOpened()):
        return 0
    
    x = 0
    while x < 20:
        ret, frame = cap.read()

        if not ret:
            # print("Unable to open frame")
            # sys.exit()
            break
        path_of_file = f"./KNOWN_FACES/{rollno}/{x}.jpg"
        cv.imshow("Person", frame)
        cv.imwrite(path_of_file, frame)
        cv.waitKey(1000)
        x += 1
    cv.destroyAllWindows()

# rolno = 'rollnumber'
# adduser(rolno)
