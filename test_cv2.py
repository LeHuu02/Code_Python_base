import cv2

print('xin chao da duoc in ra man hinh')

img = 10
print(img)

image: object  = cv2.imread('car_Parking')

#cv2.show('anh', image)
print('no co chay den dong nay khong')
cv2.waitKey()
cv2.distroyAllWindows()
