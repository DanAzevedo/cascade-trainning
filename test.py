import cv2

classifier = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = classifier.detectMultiScale(imgGray, scaleFactor=1.2)

    if len(objects) ==0:
        pass
    if len(objects) !=0:
        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

    cv2.imshow('Capture', img)
    cv2.waitKey(1)