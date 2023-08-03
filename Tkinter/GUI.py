from tkinter import * 
import tkinter.font as tkFont
import tkinter as tk

ws = Tk()
width= ws.winfo_screenwidth()
height= ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))
ws.title('PythonGuides')
f = tkFont.Font ( family="Helvetica",size=24,weight="bold")
bckpath=r"C:\Users\karth\Downloads\img.png"
bckimg=tk.PhotoImage(file=bckpath)
#print(width,height)
b_lbl=tk.Label(ws,image=bckimg)
b_lbl.place(x=0,y=0,relwidth=1,relheight=1)
def nextPage():
    ws.destroy()
    import first_page
    

def prevPage():
    ws.destroy()
    import second_page
    
Label(
    ws,
    text="Cryptography, Image Steganography and Compression Based Secured Data Hiding System",
    
    font=f,justify=CENTER,borderwidth=4,relief="solid",bg="grey",fg="#041016"
).place(x=120,y=80)
f2 = tkFont.Font( family = "Comic Sans MS", 
                                 size = 20, 
                                 weight = "bold",slant='italic')
f3=tkFont.Font(family="Arial",size=20)

Label(ws,text="Presented by",font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=630,y=580)
Label(ws,text='1.   Kailash G(124157030)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=690,y=630)
Label(ws,text='2.   Harish M R(124157024)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=690,y=680)
Label(ws,text='3.   Vikranth A(124157060)',font=f3,borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x=690,y=730)



Button(
    ws, 
    text="Image_Embedding", 
    font=f,borderwidth=4,relief="solid",bg="grey",fg="#041016",activeforeground='red',
    command=nextPage
    ).pack( expand =True,side=LEFT)

Button(
    ws, 
    text="Image_Detecting", 
    font=f,
    width=15 ,borderwidth=4,relief="solid",bg="grey",fg="#041016",activeforeground='red',
    command=prevPage
    ).pack(expand=TRUE, side=LEFT)
ws.configure()
ws.mainloop()
