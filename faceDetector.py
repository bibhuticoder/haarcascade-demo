import cv2 #opencv

#Load face cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Load Image
img = cv2.imread('people.png',cv2.IMREAD_COLOR)

#Detect faces in the image via face_cascade
faces = face_cascade.detectMultiScale(img, 1.3, 5)

#For location and size of each faces
for(x, y, w, h) in faces:

    #draw a blue rectangle
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0),  2)

#Finally show the processed image
cv2.imshow("Haarcascade Demo", img)
