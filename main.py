from tkinter import *
import tkinter.scrolledtext as sc
import threading
from bs4 import BeautifulSoup as bs
from tkinter import ttk
import requests
from PIL import Image, ImageTk

root=Tk()
root.geometry('970x560')
root.title("Social Media")
root.configure(background="whitesmoke")
image_path1 = "image/1.png"
image1 = Image.open(image_path1)
faceImage1 =  ImageTk.PhotoImage(image1)
image_path2 = "image/2.jpg"
image2 = Image.open(image_path2)
faceImage2 = ImageTk.PhotoImage(image2)
image_path3 ="image/3.png"
image3 = Image.open(image_path3)
faceImage3 = ImageTk.PhotoImage(image3)
image_path4 ="image/5.jpg"
image4 = Image.open(image_path4)
faceImage4 = ImageTk.PhotoImage(image4)
def data():
    username=en1.get()
    def face():
        face_url='https://www.facebook.com/'  
        r=requests.get(face_url+username)
        soup=bs(r.content,'html.parser')
        titlel=soup.find('title')
        al=titlel.string
        print(al)
        if al=='Aanmelden bij Facebook':
            text1.insert('end','[+] facebook:','blue')
            text1.insert('end',username,'gray')
            text1.insert('end','\n')
            text1.insert('end',face_url+username)
            text1.insert('end','[X] Not Found','red')
            text1.insert('end','\n----------------\n')
        else:
            tv.insert(parent='',index=0,image=faceImage1,values=('فيسبوك',face_url,username,'found'))     
    face()
def go():
    threading.Thread(target=data).start()
title=Label(root,text="cyberTools",font=("Courier",18),bg='black',fg='white')
title.pack(fill=X)
image_path = "1.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
banel=Label(root,image=photo)
banel.place(x=2,y=35,width="400",height="520")
l1=Label(root,text="user:")
l1.place(x=5,y=610)
en1=Entry(root,font=('Arial','12'),justify=CENTER)
en1.place(x=40,y=610,width='150',height='24')
b1=Button(root,text='Search',width='20',height='2',cursor='hand2',command=go)
b1.place(x=4,y=660)

tv=ttk.Treeview(root)
style=ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview',rowhight=35,background='#D8D8D8',fieldbackground='#D8D8D8',foreground='black')
tv['columns']=('namesocial','urlname','username','status')
tv.column('#0',anchor=CENTER,width=50)
tv.column('namesocial',anchor=CENTER,width=40)
tv.column('urlname',anchor=CENTER,width=130)
tv.column('username',anchor=CENTER,width=100)
tv.column('status',anchor=CENTER,width=30)
tv.heading('#0',text='موقع سوشيال',anchor=CENTER)
tv.heading('namesocial',text='اسم الموقع',anchor=CENTER)
tv.heading('urlname',text='رابط الموقع',anchor=CENTER)
tv.heading('username',text='اسم المستخدم',anchor=CENTER)
tv.heading('status',text='الحالة',anchor=CENTER)
tv.place(x=420,y=35,width='765',height='240')
text1=sc.ScrolledText(root)
text1['font']=('Courier','10','bold')
text1.place(x=420,y=280,width='765',height='270')
text1.tag_config('red',background='red',foreground='white')
text1.tag_config('gray',background='white',foreground='gray')
text1.tag_config('blue',background='blue',foreground='white')
root.mainloop()