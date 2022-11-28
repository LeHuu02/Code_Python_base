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

# vong lap for
# vi str1 cung la 1 list kieu chuoi string nen moi phan tu duoc coi la mot o gia tri
# moi lan in ra thi se in ra mot ky tu thu i. in tu dau den cuoi list
def lap_list():
    str1 = "xin chao cac ban"
    print("in ra cac ky tu trong chuoi: ")
    for i in str1:      #vong for nay  se in so lan bang gioi han cua str1
        print(i)

    # tuong tu voi chuoi so, co the coi list so la mot mang
    print("in ra cac phan tu trong mang")
    s = [2,3,5,7,8,9,12]
    for i in s:
        print(i)

    # in ra n phan tu trong list tu n den m, in ra n phan tu cuoi,...
    print(s[4: ])   #in ra tu phan tu vi tri thu 4 den het
    print(str1[-6:])    #in ra 6 phan tu cuoi cung trong chuoi
    print(str1[3: 8])   #in tu phan tu thu 3 den phan tu thu 7.

# range(1,10) la de tao mot list gom 10 so, chay tu 0 den 9
# bien i la bien de in ra gia tri moi lan tang len
def vonglap():
    # i = 10
    print("in tu 0 den 10-1")
    for i in range(1, 10):
        print(i)

    print("in tu 4 den 8-1")
    for i in range(4,8):
        print(i)

    # //vong lap while
    i = 0
    while i < 10:
        i = i + 1
        print("vong lap vo han neu la while True:")
        # neu bien i = 10 thi thoat khoi vong lap
        # if i == 10:
        #     break

    # khi nao nhap vao so chan thi dung lai
    nhap = 0
    while nhap % 2 == 0:
        nhap = int(input("nhap vao gia tri "))

def bai1():
    kg = int(input("nhap kg: "))
    print(kg, " kg = ", kg*1000, "gam")

def bai2():
    m = int(input("nhap met: "))
    print(m, " met = ", m*1000, "mm")
# lap_list()
# vonglap()
gt = 5
while gt != 0:
    print("0 - thoat\n1 - doi tu kg sang gam\n2 - doi tu m sang mm")
    gt = int(input("nhap gia tri: "))
    # if gt == 0:
    #     exit()
    if gt == 1:
        bai1()
    elif gt == 2:
        bai2()
    elif gt > 2:
        print("vui long nhap lai: ")