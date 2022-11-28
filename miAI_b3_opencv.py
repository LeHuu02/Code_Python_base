"""
link: miai.vn
    https://www.youtube.com/playlist?list=PLZPCoTKpEddAay-lItE-pn27uNNrApORH
    https://github.com/thangnch
power by le minh huu @LeHuu02 27/12/2022
yeu cau:
    - cac thao tac co ban trong python > 3.8
    - list: tuong tu nhu mang (so hoac chuoi string)
    - vong lap for, while, viet ham
"""

import cv2
import imutils
import numpy

def anh1():
    # doc anh
    image = cv2.imread("cho.jpg")
    # show anh
    cv2.imshow("img", image)

def video1():
    # mo camera
    cam_id = 'video1.mp4'   #doc video tu file
    cam_id = 0  #camera cong com 0
    cap = cv2.VideoCapture(cam_id)
    # doc video
    while True:
        ret, frame = cap.read() #doc tu cam
        # show video
        cv2.imshow("video cam", frame)
        # kiem tra dong anh
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

def coban():
    # image = cv2.imread("cho.jpg", cv2.COVAR_ROWS)   #doc va chuyen luon anh sang mau xam
    image = cv2.imread("cho.jpg") #doc anh
    cv2.imshow("anh con cho nay", image)
    cv2.waitKey() #cho nhan tu ban phi de thoat
    # convert mau. mac dinh la he mau BGR -> hsv, rgb, gray,...
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("con nay dak that",img_gray)

def resize():
    img = cv2.imread("cho.jpg")
    cv2.imshow("anh goc", img)
    # co the resize tuyet doi: cv2.resize(img, 299,300)
    img_rs = cv2.resize(img, dsize = None, fx = 0.5, fy = 0.5)
    cv2.imshow("anh rs",img_rs)

def xoayanh():
    # su dung thu vien ngoai import imutils
    img = cv2.imread("cho.jpg")
    cv2.imshow("anh goc", img)
    img_rotate = imutils.rotate(img, 120) #xoay anh img 120 do nguoc kim dong ho
    cv2.imshow("anh rs",img_rotate)

# chuyen anh nhi phan
def adap_threshold():
    img = cv2.imread("cho.jpg")
    cv2.imshow("anh goc", img)
    img_gary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_bir = cv2.adaptiveThreshold(img_gary, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,5, 9)
    cv2.imshow("anh nhi phan", img_bir)

# tim duong bien doi tuong: canny
def timcanh():
    img = cv2.imread("cho.jpg")
    cv2.imshow("anh goc", img)
    img_gary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img_gary, threshold1= 90, threshold2=300)
    cv2.imshow("anh nhi phan", edges)

# QUAN TRONG, TIM BIEN SO, DOC CHU
# tap hop caca diem tao duong cong kin. cac diem anh mau trang tren nen den
# ERROR NOT DROW CONTOURS
def contours():
    img = cv2.imread("anh.png")
    cv2.imshow("anh goc", img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow("hsv", img_hsv)
    cv2.waitKey()
    img_bir = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 17)
    # cont = cv2.findContours(img_bir, cv2.RETR_LIST,  cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours( img, cont, -1, (255,100,0),3)
    cv2.imshow("bin", img_bir)
    cv2.waitKey()
    contours = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    # ERROR NOT DRAW CONTOURS
    output = img.copy()
    # cv2.drawContours(output, contours, -5,  (5, 12, 253 ), 3)  # vẽ lại ảnh  contour vào ảnh gốc
    cv2.imshow("anh contours", output)

# doc video chuyen sang mau xam va hien thi len man hinh
def bai1():
    cam_id =0
    cap = cv2.VideoCapture(cam_id)
    while True:
        ret, frame = cap.read()
        if ret: #kiem tra neu doc thanh cong video thi moi thuc hien cong viec tiep theo
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("video cam", frame)
            if cv2.waitKey(1)  == ord('q'):
                break
    cap.release()

def bai11():
    cam_ip = 0
    video = cv2.VideoCapture(cam_ip)
    while True:
        ret, frame = video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("anh xam", frame)
            if cv2.waitKey(1) == ord('q'):
                break
    video.release()

#doc video. nhan phim a quay video thhanh 90 do nguoc chieu kim dong ho, phim d quay video thanh 90 do theo chieu kim dong ho
def bai2():
   vd = 'video2.mp4'
   video = cv2.VideoCapture(vd)
   roters = 0   #ban dau khong cho quay goc video
   while True:
       ret, frame = video.read()    #doc video
       if ret:  #neu doc video thanh cong thi thuc hien tiep
           if roters != 0:  #kiem tra neu goc quay khac 0 thi thay doi goc quay cua video
               frame = imutils.rotate(frame, roters)    #thay doi goc cua fram
           cv2.imshow("video nay", frame)
       # kiem tra xem nhap vao ky tu gi
       key = cv2.waitKey(40)
       if key == ord('a'):  #neu nhap vao a quay video 90 do
           # roters = 0
           roters = 90
       elif key == ord('q'):    #nhap q quay 270 do
           # roters = 0
           roters = 270
       elif key == ord('x'):   #neu nhap vao x thi quay lai vi tri ban dau
           roters = 0
       elif key == ord('d'):  #neu nhap vao d thi thoat video
           break

def bai3():
    print("x")


# coban()
# resize()
# xoayanh()
# video1()
# adap_threshold()
# timcanh()
# contours()
# bai1()
# bai11()
# bai2()
bai3()

# dung man hinh
cv2.waitKey()
# dong tat ca cac cua so
cv2.destroyAllWindows()
