"""
link: miai.vn
    https://www.youtube.com/playlist?list=PLZPCoTKpEddAay-lItE-pn27uNNrApORH
    https://github.com/thangnch
power by le minh huu @LeHuu02 27/12/2022
yeu cau:
    - cac thao tac co ban trong python > 3.8
    - nhap xuat, gan gia tri, ham con, dieu kien so sanh, ep kieu,..
"""
print("xin chao toi da tro lai roi")
print("dung gian nua nha Lam, xin loi ma :((")

# NOTE: mac dinh khi nhap vao thi se la kieu chuoi string -> phai ep kieu

# nhap mot so in ra binh phuong so do
def binhphuong():
    so = input("nhap vao mot so:")
    so = int(so)
    print("binh phuong so la: ", so**2)

# nhap ten tuoi mot  nguoi, roi xem tuoi la bao nhieu va chao
def nhap():
    ten = input("nhap vao ten:")
    tuoi = input("nhap vao tuoi:")
    tuoi = int(tuoi)    #ep kieu sang kieu int
    if tuoi < 10:
        print("chao chau ", ten)
    elif 10 <= tuoi < 30:
        print("chao ban ", ten)
    elif 30 <= tuoi < 60:
        print("chao bac "+ ten)
    elif tuoi >= 60:
        print("chao ong", ten)
    else:
        print("xin chao")

# nhap vao 3 so, so sanh va tim so lon nhat
def sosanh(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    max = a
    if max < b: max = b
    if max < c: max = c
    print("so lon nhat la: ", max)

#     so sanh
    if a == b:
        print("so a bang so b")
    elif a == c:
        print("so a bang so c")
    else:
        print("ban tu di ma so sanh toi chiu")

binhphuong()
nhap()
sosanh(7,12,5)