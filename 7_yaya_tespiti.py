#  yaya tespiti
import cv2
import os

# files = os.listdir()
# print(files)

images = ["p1.jpeg", "p2.jpeg"]

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for image in images:
    img = cv2.imread(image)

    (rects, weigths) = hog.detectMultiScale(img, padding=(8,8), scale=1.05)

    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

    cv2.imshow("yaya", img)

    if cv2.waitKey(0) & 0XFF == ord('g') : continue

