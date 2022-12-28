#dong ho dem gio
from tkinter import *
import time
root=Tk()
stringt1=StringVar()
stringt2=StringVar()
min=0
sec=0
start_times = time.strftime("%S")
run=True
def rsAction():
    global min
    global sec
    global run
    stringt1.set("")
    stringt2.set("")
    min=0
    sec=0
    run=False

def Start():
    global min
    global sec
    run=True
    while run==True:
        stringt2.set(str(sec))
        stringt1.set(str(min))
        if sec==60:
            min+=1
            sec=0
        root.update()  # update time
        time.sleep(1)
        sec+=1

def pauseAction():
    global run
    run=False
    while run==False:
        stringt2.set(str(sec))
        stringt1.set(str(min))
        root.update()  # update time
        time.sleep(1)




root.title("Sieu Dong Ho")
root.resizable(height=True,width=True)
root.minsize(height=100,width=260)

frameButton1=Frame()
frameButton2=frameButton3=frameButton4=Frame()

Button(frameButton1,text="Start",width=11,command=Start).pack(side=LEFT)
frameButton1.place(x=5,y=5)

Time1=Entry(root,width=20,textvariable=stringt1).place(x=2,y=40)
Time1=Entry(root,width=20,textvariable=stringt2).place(x=130,y=40)

Button(frameButton2,text="Thoát",width=11,command=root.quit).pack(side=LEFT)
frameButton2.place(x=2,y=70)
Button(frameButton3,text="Reset",width=11,command=rsAction).pack(side=LEFT)
frameButton3.place(x=2,y=70)
Button(frameButton4,text="Pause",width=11,command=pauseAction).pack(side=LEFT)
frameButton4.place(x=2,y=70)

root.mainloop()