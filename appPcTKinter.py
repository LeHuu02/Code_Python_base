'''
code by le minh huu - ictu @LeHuu02 @copyright cnleminhhuu@gmail.com
project app computer TKinter 12/2022
power by: https://www.youtube.com/watch?v=ji8pTynQhEo&list=PL9A3Oc9C8D_ke0nLPzGUU-4hmq7ywb6rj&index=26
'''
from tkinter import *
import os
os.system('clear')

#######################
#TKinter GUI
#######################
root = Tk()
root.title('debuger by HUU')
root.geometry("200x100")

def works():
    work_label = Label(root, text ="hello" + myTextbox.get())
    work_label.pack()

myLabel = Label(root, text ="enter your data")
myLabel.pack()
myTextbox = Entry(root, width=30)
myTextbox.pack()

myButton = Button(root, text="send data", command = works)
myButton.pack()

root.mainloop()