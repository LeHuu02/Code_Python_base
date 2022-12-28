'''
power by code by le minh huu - ictu @LeHuu02 @copyright cnleminhhuu@gmail.com
project app computer TKinter 12/2022
 https://www.youtube.com/watch?v=ji8pTynQhEo&list=PL9A3Oc9C8D_ke0nLPzGUU-4hmq7ywb6rj&index=26
'''
from tkinter import *
import os
os.system('clear')

#######################
#TKinter GUI
#######################
root = Tk()
root.title('debuger by Le Minh Huu')
root.geometry("300x200")        #cau hinh chieu dai rong cua cua so hien thi

'''hien thi chu va o nhap du lieu: width, height'''
width = Label(root, text ="detect: width")
width.pack()
myTextbox_width = Entry(root, width=20)
myTextbox_width.pack()

height = Label(root, text ="detect: height")
height.pack()
myTextbox_height = Entry(root, width=20)
myTextbox_height.pack()

'''ham lam viec: khi nhat button thi se gui du lieu vua nhap len man hinh'''
'''luu du lieu vua nhap vao hai bien width va height'''
def works():
    width_label = Label(root, text ="width: " + myTextbox_width.get())
    height_label = Label(root, text="heght: " + myTextbox_height.get())
    width_label.pack()
    height_label.pack()
    dataWidth = myTextbox_width.get()
    dataHeight = myTextbox_height.get()
    # print("data width: " + dataWidth)
    # print("data heghth: " + dataHeight)

'''su kien nut nhan button'''
myButton = Button(root, text="send data", command = works)
myButton.pack()

'''doc du lieu va luu lai'''
dataWidth = myTextbox_width.get()
dataHeight = myTextbox_height.get()
print("data width: " + dataWidth)
print("data heghth: " + dataHeight)

'''vong lap tuan hoan den khi nao exit'''
root.mainloop()