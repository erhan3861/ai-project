import cv2
import matplotlib.pyplot as plt

tesla = cv2.imread("tesla.jpg", 0)
plt.figure()
plt.imshow(tesla, cmap="gray")
plt.axis("off")
plt.show()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# face_rect = face_cascade.detectMultiScale(tesla)
#
# for (x,y,w,h) in face_rect:
#     cv2.rectangle(tesla, (x,y), (x+w, y+h), (255,0,255), 5)
#
# plt.figure()
# plt.imshow(tesla, cmap="gray")
# plt.axis("off")
# plt.show()
#
# tr = cv2.imread("tr.jpg", 0)
# plt.figure()
# plt.imshow(tr, cmap="gray")
# plt.axis("off")
# plt.show()
#
# face_rect = face_cascade.detectMultiScale(tr, minNeighbors=5)
# for (x,y,w,h) in face_rect:
#     cv2.rectangle(tr, (x,y), (x+w, y+h), (255,0,255), 5)
#
# plt.figure()
# plt.imshow(tr, cmap="gray")
# plt.axis("off")
# plt.show()

# video
cap = cv2.VideoCapture(0) # 0 -> dahili cam    1 -> webcam

while True:
    ret, frame = cap.read()

    if ret: # geri dönüş varsa ret True
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors=7)
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 7)

    cv2.imshow("Face", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



















