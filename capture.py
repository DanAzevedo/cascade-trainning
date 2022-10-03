import cv2

cap = cv2.VideoCapture(0)
sample = 1

while True:
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        imgR = cv2.resize(imgGray, (220, 220))
        cv2.imwrite(f'positives/im-{sample}.jpg', imgR)
        sample += 1

    cv2.imshow('Capture', img)
    cv2.waitKey(1)