import cv2 as cv
import sys
import os
import face_recognition
import time

def isPresent(rollno):
    known_faces = []
    # roll_no_present = os.listdir('KNOWN_FACES')
    # print(os.listdir('KNOWN_FACES'))
    if not(rollno in os.listdir('KNOWN_FACES')):
        return -1
    # Loading data of images
    for imgname in os.listdir(f"KNOWN_FACES/{rollno}"):
        if not(imgname[0] == '.'):
            img = face_recognition.load_image_file(f"KNOWN_FACES/{rollno}/{imgname}")
            try:
                encoding = face_recognition.face_encodings(img)[0]
            except:
                # print(f"Unable to find face in {imgname}")
                pass
            known_faces.append(encoding)
    
    # Testing if person present
    cap = cv.VideoCapture(0)
    if not(cap.isOpened()):
        # sys.exit("Unable to open camera")
        return 0
    
    
    initial = time.time()
    while(time.time() - initial <= 20):
        # print(time.time()-initial)
        retrn, frame = cap.read()
        locations = face_recognition.face_locations(frame, model="cnn")
        encoding = face_recognition.face_encodings(frame, locations)

        for face_encoding, face_location in zip(encoding,locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, 0.6)
            # return True in results
            if (True in results):
                return 1


# print(isPresent("isav"))
if __name__ == '__main__':
    print(isPresent('123'))
        


