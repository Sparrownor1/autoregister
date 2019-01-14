import cv2
import os
from UserList import *

# NOTE: Create folders for each new user
users = open("UserList.txt", "r")
userDatabase = getUserList(users)
users.close()

#Initialize userID
userID = 0
#Input UserID
while (userID not in userDatabase):
    try:
        userID = int(input("Enter your 4-digit userID\n"))
        break
    except typeError:
        pass
# os.mkdir("dataset/" + str(userID))

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

face_detector = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.4.2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

count = 0
maxPictures = 30

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/" + str(userID) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= maxPictures:  # Take 30 face sample and stop video
        break

# Do a bit of cleanup
# print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
