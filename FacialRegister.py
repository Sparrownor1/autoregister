import cv2
import numpy as np
import os
from UserList import *

# NOTE: To Do: Adding pictures to training data
# NOTE: To Do: Add faces not to predict
# NOTE: To Do: Date and Time and Timetable
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#Initialize ID value
id = 0

# def checkFace(userName):
#     checkface = input("Are you " + str(userName + '\n'))
#     if checkface == 'y':
#         #doSomething
#         return True
#     elif checkface == 'n':
#         return False
#         #Should not predict same User again


users = open("UserList.txt", "r")
userDatabase = getUserList(users)
users.close()

###MUST PUT THIS ALL IN A WHILE LOOP

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while(True):

    breakloop = False #Initialize breakloop
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for(x, y, w, h) in faces:

        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imshow('camera', img)
        #
        id, error = recognizer.predict(gray[y:y + h, x:x + w])

        if (error < 100):
            userName = userDatabase[id]
            confidence = round(100 - error)
            # check = checkFace(userName)
            cv2.imshow(" ", img)
            cv2.waitKey(3000)
            checkface = input("Are you " + str(userName + '\n' + "Confidence: " + str(confidence) + '\n'))
            if checkface == 'y':
                cv2.imwrite("dataset/User." + str(id) + '.' + '30' + ".jpg", gray[y:y + h, x:x + w])
                breakloop = True
                #write image
            elif checkface == 'n':
                pass
                #Should not predict same User again


        # if check == True:
        #     breakloop = True
        #     break


        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
    if breakloop == True:
        break

cam.release()
cv2.destroyAllWindows()
