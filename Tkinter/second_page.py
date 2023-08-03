import tkinter as tk
import os
from tkinter import *
import Decompression_DWT as dcd
import AES_Hash_Decryption as dt
import stegno_decoded as decod
from tkinter import filedialog
import tkinter.font as tkFont
import time
import txtimage as txim
from PIL import Image, ImageTk
sg = Tk()
width= sg.winfo_screenwidth()
height= sg.winfo_screenheight()
sg.geometry("%dx%d" % (width, height))
bckpath=r"C:\Users\karth\Downloads\img.png"
bckimg=tk.PhotoImage(file=bckpath)
#print(width,height)
b_lbl=tk.Label(sg,image=bckimg)
b_lbl.place(x=0,y=0,relwidth=1,relheight=1)
sg.title('Detecting')
def get_file_path():
    global file_path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("jpg","*.jpg"),("PNG","*.png"),("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
cbt=("Arial",16)
f = ("Times bold", 14)

def helloCallBack():
    global C1,lbl,decrypted_img
    decod.extract_data_from_image(file_path)
    C1.select()
    txim.txt_to_image()
    lbl.place(x=360,y=410)
    lbl.config(text="SUCCESSFUL",foreground="green",font=cbt)
    decrypted_img = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\detect_aes.jpg")
    decrypted_img= decrypted_img.resize((200,200))
    decrypted_img = ImageTk.PhotoImage(decrypted_img)
    label1 = tk.Label(image=decrypted_img)
    label1.image = decrypted_img
    label1.place(x=325, y=460)  

def helloCallBack1():
    global C2,lb2,key,aesimg
    dt.decrypt(key)
    time.sleep(1)
    C2.select()
    lb2.place(x=680,y=410)
    lb2.config(text="SUCCESSFUL",foreground="green",font=cbt)
    aesimg = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\nonsteg11_33_59decry.png")
    aesimg= aesimg.resize((200,200))
    aesimg = ImageTk.PhotoImage(aesimg)
    label2 = tk.Label(image=aesimg)
    label2.image = aesimg
    label2.place(x=650, y=460) 
      
def helloCallBack2():
    global C3,lb3,decomp
    otpath=r"C:\Users\karth\OneDrive\Desktop\Mini Project\nonsteg11_33_59decry.png"
    dcd.Decompression_Process(otpath)
    #time.sleep(1)
    C3.select()
    lb3.place(x=1030,y=410)
    lb3.config(text="SUCCESSFUL",foreground="green",font=cbt)
    decomp = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\Decompressed\decompressed.jpg")
    decomp= decomp.resize((200,200))
    decomp = ImageTk.PhotoImage(decomp)
    label3 = tk.Label(image=decomp)
    label3.image = decomp
    label3.place(x=1010, y=460) 


def back():
    sg.destroy()
    import GUI  
fst = tkFont.Font ( family="Helvetica",size=18)

user_name = Label(sg,font=fst,
                  text = "Image_path",borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x = 600,
                                           y = 100) 
def get_key():
    global key
    key=textbox.get()
 
lbl = Label(sg)
lb2 = tk.Label(sg, text = "")
lb2.place(x=233,y=200)
lb3=tk.Label(sg,text="")

compress=tk.Label(sg,text="Stegnography Decoding",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
compress.place(x=315,y=300)
C1 = Checkbutton(sg  ,borderwidth=4,relief="solid",fg="#041016")  
C1.place(x=285,y=300)
B=tk.Button(sg,text="Click",command= helloCallBack,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B.place(x=395,y=360)

encrypt=tk.Label(sg,text="DeCryption(AES)",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
encrypt.place(x=650,y=300)
C2 = Checkbutton(sg ,borderwidth=4,relief="solid",fg="#041016" )  
C2.place(x=620,y=300)
B1=tk.Button(sg,text="Click",command= helloCallBack1,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B1.place(x=730,y=360)

embed=tk.Label(sg,text="Decompression(DWT)",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
embed.place(x=980,y=300)
C3 = Checkbutton(sg ,borderwidth=4,relief="solid",fg="#041016" )  
C3.place(x=950,y=300)
B1=tk.Button(sg,text="Click",command=helloCallBack2,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B1.place(x=1070,y=360)

fbt = Button(sg, text = "Open File", command = get_file_path,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
fbt.place(x=750,y=105)
bck=tk.Button(sg,text="BACK",foreground='red',command=back,justify=CENTER)
bck.place(x=760,y=760)
klbl=tk.Label(sg,text="Password",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
klbl.place(x=600,y=150)
textbox = Entry(sg, bg="white",width=40,borderwidth=2,relief="solid",fg="#041016",font=("Arial",12))
textbox.place(x=720,y=160)
cpy=tk.Button(sg,text='SUMIT',command=get_key,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
cpy.place(x=1085,y=157)

sg.configure()
sg.mainloop()
