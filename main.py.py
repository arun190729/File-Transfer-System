from PIL import ImageTk, Image
from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import ImageTk, Image



root=Tk()
root.title("File Transfer")
root.geometry("450x560+500+200")
root.configure(bg="")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('file_type','*.txt'),('all files','*.*')))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("Waiting for Connection.....")
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data transfered successfully.....")



    img=PhotoImage(file="Image/send.png")
    window.iconphoto(False,img)

    img3=Image.open("Image/FILESS.png")
    img3=img3.resize((453,250))
    Sbackground=ImageTk.PhotoImage(img3)
    Label(window,image=Sbackground).place(x=-2,y=10)

    img4=Image.open("Image/joker.png")
    img4 = img4.resize((90,90))

    mbackground=ImageTk.PhotoImage(img4)
    Label(window,image=mbackground,bg="teal").place(x=190,y=380)

    Button(window,text="+Select File",width=10,height=1,font='arial 14 bold',bg="teal",fg="#000",command=select_file).place(x=60,y=230)
    Button(window, text="Send", width=10, height=1, font='arial 14 bold', bg="TEAL", fg="#000",command=sender).place(x=280,y=230)
    host=socket.gethostname()
    Label(window,text=f'ID: {host}',bg='White',fg='black').place(x=190,y=360)
    window.mainloop()



def Received():
    main=Toplevel(root)
    main.title("Received")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File Received Successfully")

    img=PhotoImage(file="Image/receive.png")
    main.iconphoto(False,img)

    # img7=Image.open("Image/bg2.png")
    # img7=img7.resize((460,90))
    #
    # back=ImageTk.PhotoImage(img7)
    # Label(main,image=back).place(x=0,y=0)

    img5 = Image.open("Image/trans.png")
    img5= img5.resize((450, 225))

    hbackground = ImageTk.PhotoImage(img5)
    Label(main,image=hbackground).place(x=0,y=0)

    img6=Image.open("Image/RE.png")
    img6=img6.resize((90,90))

    logo=ImageTk.PhotoImage(img6)
    Label(main,image=logo).place(x=30,y=230)


    Label(main,text="Receive..",font=('arial',20),bg="white").place(x=140,y=260)

    Label(main,text="Input Sender id",font=('arial',10,'bold'),bg="cyan").place(x=20,y=330)
    SenderID=Entry(main,width=25,fg="black",border=2,bg="white",font=("arial",15))
    SenderID.place(x=20,y=350)
    SenderID.focus()

    Label(main, text="filename for the incoming file", font=('arial', 10, 'bold'), bg="cyan").place(x=20, y=380)
    incoming_file= Entry(main, width=25, fg="black", border=2, bg="white", font=("arial", 15))
    incoming_file.place(x=20, y=400)

    rr=Button(main,text="RECEIVE",compound=LEFT,width=10,bg="teal",font="arial 10 bold",command=receiver)
    rr.place(x=20,y=450)

    main.mainloop()





#icon
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,'bold'),bg="wheat").place(x=20,y=30)
Frame(root,width=400,height=2,bg="coral").place(x=25,y=80)

img1=Image.open("Image/send1.png")
img1=img1.resize((80,80))

send_image=ImageTk.PhotoImage(img1)
send=Button(root,image=send_image,bg="gold",bd=0,command=Send)
send.place(x=50,y=100)

img=Image.open("Image/receive1.png")
img=img.resize((80,80))


receive_image=ImageTk.PhotoImage(img)
receive=Button(root,image=receive_image,bg="pink",bd=0,command=Received)
receive.place(x=300,y=100)

Label(root,text="Send",font=("Acumin Variable Conceot",17,'bold'),bg="white").place(x=60,y=184)
Label(root,text="Receive",font=("Acumin Variable Conceot",17,'bold'),bg="white").place(x=296,y=180)

img2=Image.open("Image/files.jpg")
img2=img2.resize((460,220))

background=ImageTk.PhotoImage(img2)
Label(root,image=background).place(x=-2,y=285)

root.mainloop()


