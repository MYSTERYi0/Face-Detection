"""
Face detection Using Python
"""

import cv2

# ________________________________________Detects the faces in an image______________________________________

# facecascade = cv2.CascadeClassifier(r'C:\Users\Aryan Gupta\PycharmProjects\Image processing\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# faceimg = cv2.imread('venv/Scripts/Faces.jpg')
# faceimgresized = cv2.resize(faceimg, (500, 500))
# imggray = cv2.cvtColor(faceimgresized, cv2.COLOR_BGR2GRAY)
# face = facecascade.detectMultiScale(imggray)  # Detects the face features
# for (x, y, w, h) in face:  # for multiple faces
#     cv2.rectangle(faceimgresized, (x, y), (x + w, y + h), (0, 255, 0, 2))
#
# cv2.imshow('Face Output', faceimgresized)
# cv2.waitKey(0)

# ____________________________Face detection using Video cam (Real time)_______________________________________
cap = cv2.VideoCapture(0)  # Triggers the camera
cap.set(3, 480)  # cap.set() has 2 args 1. property ID and 2. value of propID.
cap.set(4, 480)  # Refer documentation for codes
cap.set(10, 150)  # The IDs 3, 4, 10 are for ht, width, brightness resp

facecascade = cv2.CascadeClassifier(r'C:\Users\Aryan Gupta\PycharmProjects\Image processing\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    frame_flip = cv2.flip(frame, 1)
    bw_video = cv2.cvtColor(frame_flip, cv2.COLOR_BGR2GRAY)
    face = facecascade.detectMultiScale(bw_video, 1.1, 4)
    for (x, y, w, h) in face:  # For loop used to create rectangle for every frame of the Video
        cv2.rectangle(frame_flip, (x, y), (x + w, y + h), (255, 0, 0, 3))  # Creates a rectangle around the face
    cv2.imshow('Aryan', frame_flip)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()  # To release the device, which frees the camera port to be usable next time wo raising errors
cv2.destroyAllWindows()  # destroy all window
