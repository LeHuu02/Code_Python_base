# comment mot dong
"""
day la comment nhieu dong:
power by le minh huu 27/12/2022 @LeHuu02 @copyright
read me:
    - nhap xuat co ban: nhap xuat so, chuoi ky tu, mang mot chieu,...
    - cau lenh dieu kien if else, switch case
    - vong lap while, for, do while,...
    - bai toan co ban.
"""

# in ra tong cua hai so
data = 1208
sum = data + 2000
print(sum)

"""
# nhap mot so va mot chuoi string
# print("nhap vao mot so va in ra man hinh: ")
# n = input()
# print("so vua nhap la: "+n)
# print("nhap vao mot chuoi: ")
# str = input()
# print("chuoi vua nhap la: "+str)
"""


# cau lenh if else: so sanh 3 so tim so lon nhat
print("nhap vao ba so a b c: ")
a = input()
b = input()
c = input()
print("so vua nhap: "+a+"\t"+b+"\t"+c)

# tim max
max = int(a)
if max < int(b): 
    max = b
if int(max) < int(c): 
    max = c
print("so lon nhat trong ba so la: "+max)

# so sanh hai so a b
if int(b) == int(a):
    print("so "+a+" = so "+b)
else:
    print("so "+a+" khong bang so "+b)

# so sanh max voi so 123
x = 123
if int(max) > int(x):
    print("max = "+max+" lon hon so 123")
else:
    print("max = "+max+" nho hon so 123")
    
# kiem tra if else
z = 5
c = int(a) + int(z)
# print("z = 5, tong z + a = "+c)
if int(z) == int(a):
    print("so a la so nam")
else:
    print("so a khong phai so nam")



# # switch case:
# # print("nhap vao thu: ")
# thu = input("nhap vao thu: ")
# switcher = {
#     1:'so mot',
#         # print("so mot a"),
#     2:'so hai'
#         # print("thu 2")
#
#
# }
# # print(switcher.get(thu))
# # switcher.get(thu, "so nay khong biet")
# print(switcher.get(thu,"so nay khong biet"))


