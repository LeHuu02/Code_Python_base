'''
Bài 3: Đọc ảnh từ một webcam, nhận diện các khuôn
mặt và vẽ một hình chữ nhật màu xanh Green quanh
khuôn mặt. Đếm số khuôn mặt có trong hình. Nếu
người dùng nhấn phím S thì lưu các khuôn mặt đó ra
các file ảnh 0.png, 1.png, 2.png…. (tùy số lượng
khuôn mặt)
'''
import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def save_face(frame, faces):
    i=0
    for (x, y, w, h) in faces:
        i+=1
        crop = frame[y:y+h,x:x+w]
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.imwrite("file{}.png".format(i),crop)
    return
camera = cv.VideoCapture(0)

while (True):
    ret, img = camera.read()
    if ret:
        # Chuyen gray
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 10,minSize=(100,100))

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            qroi_color = img[y:y + h, x:x + w]

        cv.imshow("Picture", img)

    key = cv.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('s'):
        save_face(img, faces)

camera.release()
cv.destroyAllWindows()

