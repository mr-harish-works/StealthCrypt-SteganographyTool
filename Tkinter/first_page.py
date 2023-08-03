import tkinter as tk
import os
from tkinter import *
import compress_new2 as cd
import AES_Hash as en
import time
from tkinter import filedialog
import tkinter.font as tkFont
import pyperclip
import img_txt as imt
import stegnno_embed as embd
import Performance_Metrics as pm
from PIL import Image, ImageTk

key=''
sg = Tk()
width= sg.winfo_screenwidth()
height= sg.winfo_screenheight()
sg.geometry("%dx%d" % (width, height))
sg.title('Embedding')
f = ("Times bold", 14)
bckpath=r"C:\Users\karth\Downloads\img.png"
bckimg=tk.PhotoImage(file=bckpath)
#print(width,height)
b_lbl=tk.Label(sg,image=bckimg)
b_lbl.place(x=0,y=0,relwidth=1,relheight=1)
def get_file_path():
    global file_path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("jpg","*.jpg"),("PNG", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))

def get_file_path1():
    global cvr_file_path
    cvr_file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("jpg","*.jpg"),("PNG", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
def submit():
    global key_name
    key_name = textbox.get()
    #lbl.config(text = "Provided Input: "+inp)
cbt=("Arial",16)
def helloCallBack():
    global C1,lbl,img,comp_image
    #path=r"C:\Users\karth\OneDrive\Desktop\40_percent\image_source\download (1).jpg"
    comp_image=cd.Compression_Process(file_path)
    #time.sleep(1)
    C1.select()
    lbl.place(x=400,y=410)
    lbl.config(text="SUCCESSFUL",foreground="green",font=cbt)

    #img = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\Stegnography\jerald_savior.png")
    comp_image = comp_image.resize((200,200))
    comp_image = ImageTk.PhotoImage(comp_image)
    label1 = tk.Label(image=comp_image,)
    label1.image = comp_image

    label1.place(x=360, y=460)    
  


      
def helloCallBack1():
    global key,textbox,key_name
    global C2,lb2,img1,image_Encypted
    otpath=r"C:\Users\karth\OneDrive\Desktop\Mini Project\c1.jpg"
    #print(key_name)
    key=en.encrypt(otpath,key_name)
    print(key)
    #textbox.insert(0, key)
    print(key_name)
    C2.select()
    imt.txtconvert()
    lb2.place(x=700,y=410)
    lb2.config(text="SUCCESSFUL",foreground="green",font=cbt)
    image_Encypted = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\aes_gui_trail.png")
    image_Encypted = image_Encypted.resize((200,200))
    image_Encypted = ImageTk.PhotoImage(image_Encypted)
    label1 = tk.Label(image=image_Encypted,)
    label1.image = image_Encypted
    label1.place(x=680, y=460) 

def helloCallBack2():
    global C3,lb3,img2,cvr_file_path
    path=r"C:\Users\karth\OneDrive\Desktop\Mini Project\gui_trail.txt" 
    embd.hide_data_in_image(path,cvr_file_path)
    C3.select()
    lb3.place(x=1000,y=410)
    lb3.config(text="SUCCESSFUL",foreground="green",font=cbt)
    img2 = Image.open(r"C:\Users\karth\OneDrive\Desktop\Mini Project\gui_trail_steg.png")
    img2 = img2.resize((200,200))
    img2 = ImageTk.PhotoImage(img2)
    label1 = tk.Label(image=img2,)
    label1.image = img2
    label1.place(x=980, y=460) 
    #cvr_path=r"C:\Users\karth\OneDrive\Desktop\Mini Project\cover1.jpg"
    steg_path=r"C:\Users\karth\OneDrive\Desktop\Mini Project\gui_trail_steg.png"
    ssim=pm.ssim_indx(cvr_file_path,steg_path)
    ssim_txt.insert(0,ssim)
    psnr=pm.psnr_indx(cvr_file_path,steg_path)
    psnr_txt.insert(0,psnr)

def back():
    sg.destroy()
    import GUI  
fst = tkFont.Font ( family="Helvetica",size=18)

user_name = Label(sg,font=fst,
                  text = "Secret-Image",borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x = 600,
                                           y = 100) 
def copy():
    global textbox
    txt=textbox.get()
    pyperclip.copy(txt)



 
lbl = Label(sg)
lb2 = tk.Label(sg, text = "")
lb2.place(x=233,y=200)
lb3=tk.Label(sg,text="")
compress=tk.Label(sg,text="Compress Image(DWT) ",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
compress.place(x=350,y=300)
C1 = Checkbutton(sg ,borderwidth=4,relief="solid",fg="#041016")   
C1.place(x=320,y=300)
B=tk.Button(sg,text="Click",command= helloCallBack,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B.place(x=450,y=360)

encrypt=tk.Label(sg,text="Encryption(AES) ",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
encrypt.place(x=700,y=300)
C2 = Checkbutton(sg ,borderwidth=4,relief="solid",fg="#041016" )  
C2.place(x=670,y=300)
B1=tk.Button(sg,text="Click",command= helloCallBack1,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B1.place(x=770,y=360)

embed=tk.Label(sg,text="Steganography(LSB) ",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
embed.place(x=980,y=300)
C3 = Checkbutton(sg ,borderwidth=4,relief="solid",fg="#041016" )  
C3.place(x=950,y=300)
B2=tk.Button(sg,text="Click",command=helloCallBack2, background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
B2.place(x=1070,y=360)

fbt = Button(sg, text = "Open File", command = get_file_path,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
fbt.place(x=750,y=105)

cover_name = Label(sg,font=fst,
                  text = "Cover-Image",borderwidth=4,relief="solid",bg="grey",fg="#041016").place(x = 600,
                                           y = 150) 
fbt = Button(sg, text = "Open File", command = get_file_path1,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
fbt.place(x=750,y=155)

bck=tk.Button(sg,text="BACK",foreground='red',command=back,justify=CENTER)
bck.place(x=20,y=760)

ktxt=tk.Label(sg,text='Password',font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
ktxt.place(x=600,y=200)
textbox = Entry(sg, bg="white",width=40,borderwidth=2,relief="solid",fg="#041016",font=("Arial",12))
textbox.place(x=720,y=205)
sbmt=tk.Button(sg,text='Submit',command=submit,background='CadetBlue1',
          activeforeground='red', borderwidth=3,relief="solid")
sbmt.place(x=1090,y=203)

metrics=tk.Label(sg,text="Performance Metrics",font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
metrics.place(x=660,y=700)

psnr=tk.Label(sg,text='PSNR',font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
psnr.place(x=450,y=740)
psnr_txt = Entry(sg, bg="white", width=30)
psnr_txt.place(x=530,y=747)

ssim=tk.Label(sg,text='SSIM',font=fst,borderwidth=4,relief="solid",bg="grey",fg="#041016")
ssim.place(x=890,y=740)
ssim_txt = Entry(sg, bg="white", width=30)
ssim_txt.place(x=960,y=747)



sg.configure() #azure cornsilk
sg.mainloop()
