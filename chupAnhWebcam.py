import cv2

def takephoto():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # show anh
    cv2.imshow('anh',frame)
    # chup va luu lai anh
    cv2.imwrite('photo.jpg', frame)
    cap.release()

while(True):
    takephoto()
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

