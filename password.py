from tkinter import *
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
root=Tk()
root.geometry('290x500')
root.title('Screen Lock')
image = Image.open('key.ico')  # استخدم صورة بتنسيق PNG أو JPG
photo = ImageTk.PhotoImage(image)
root.call('wm', 'iconphoto', root._w, photo)
root.iconbitmap('key.ico')
root.resizable(False,False)
root.attributes('-alpha',0.8)
def reset(enent=None):
    en1.delete('0',END)
def one(enent=None):
    one=1
    en1.insert(END,one)
def Two(enent=None):
    two=2
    en1.insert(END,two)
def three(enent=None):
    three=3
    en1.insert(END,three)
def fore(enent=None):
    fore=4
    en1.insert(END,fore)
def five(enent=None):
    five=5
    en1.insert(END,five)
def six(enent=None):
    six=6
    en1.insert(END,six)
def seven(enent=None):
    seven=7
    en1.insert(END,seven)
def ait(enent=None):
    ait=8
    en1.insert(END,ait)
def nine(enent=None):
    nine=9
    en1.insert(END,nine)
def zero(enent=None):
    zero=0
    en1.insert(END,zero)  
def corect():
    password=en1.get()
    import os
    if password=='123456':
       os.startfile(r'C:\Users\Alaa\AppData\Local\ScratchJr\ScratchJr.exe')
    if password!='123456':
        global error1
        error1=Label(f1,text='Error Password',fg='red',bg='white')
        error1.place(x=100,y=100)
        s=cv2.VideoCapture(0)
        ret,image=s.read()
        cv2.imwrite('lock.png',image)
        del(s)

title=Label(root,text='Screen Lock',background='red',fg='white',font=('Stencil',21))
title.pack(fill=X)
f1=Frame(root,bg='white')
f1.place(x=1,y=38,width=298,height=460)
title1=Label(f1,text='Enter Password',bg='white',fg='black',font=('Stencil',15))
title1.place(x=55,y=10)
en1=Entry(f1,justify=CENTER,font=('Impact',25),bd=2,relief=RAISED,width=10,bg='white',fg='red')
en1.place(x=50,y=50)
b1=Button(f1,text='1',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=one)
b1.place(x=20,y=130)
b2=Button(f1,text='2',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=Two)
b2.place(x=110,y=130)
b3=Button(f1,text='3',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=three)
b3.place(x=200,y=130)
b4=Button(f1,text='4',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=fore)
b4.place(x=20,y=215)
b5=Button(f1,text='5',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=five)
b5.place(x=110,y=215)
b6=Button(f1,text='6',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=six)
b6.place(x=200,y=215)
b7=Button(f1,text='7',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=seven)
b7.place(x=20,y=300)
b8=Button(f1,text='8',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=ait)
b8.place(x=110,y=300)
b9=Button(f1,text='9',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=nine)
b9.place(x=200,y=300)
b10=Button(f1,text='❌',font=('Stencil',25),fg='red',bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=reset)
b10.place(x=20,y=385)
b11=Button(f1,text='0',font=('Stencil',25),bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=zero)
b11.place(x=110,y=385)
b12=Button(f1,text='✔',font=('Stencil',25),fg='green',bg='white',bd=0,relief=GROOVE,width=3,cursor='hand2',command=corect)
b12.place(x=200,y=385)
root.mainloop()