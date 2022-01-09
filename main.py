from tkinter import*
from tkinter import messagebox
def user():
    user = USERNAME.get()

    pas = PASSWORD.get()


    if user == "" or pas == "":
        messagebox.showerror(title="Error", message="fill planks")

    elif x.get()==0:
        messagebox.showerror(title="Error", message="check the agree box")
    else:

        messagebox.showinfo(title="Info",message="Wolcome to web tool \n"+user)

        print("user name:-" + user)
        print("password :-" + pas)
def chech():
    if x.get()== 1:
        print("you are agtee")
    else:
        print("you don't agree")
def who():
    messagebox.showinfo(message="I am unknown but you can call me last distiny")


wid= Tk()

x= IntVar()

background=PhotoImage(file="images (1).png")
photo= PhotoImage(file="images (1).png")

wid.title("sing in")
wid.config(background="black")
wid.iconphoto(True,photo)
wid.geometry("800x400")

bg=Label(wid,image=background).place(x=480 ,y=100)
username=Label(wid,text="USER NAME",font=("classic",9,"bold"),fg="#00FF00",bg="black").place(x=230,y=200)
password=Label(wid,text="PASSWORD",font=("classic",9,"bold"),fg="#00FF00",bg="black").place(x=230,y=230)
textlogin=Label(wid,text="Web Tools",font=("roman",40,"bold"),fg="#00FF00",bg="black" ).place(x=300,y=15)
copyright=Label(wid,text="2022 created by %ALSRKAL% :)",
                font=("Arial",10),fg="yellow",bg="black").place(x=300,y=370)

box1=Checkbutton(wid,text="check here if you agree",font=("classic",10,),fg="#00FF00",bg="black",activeforeground="#00FF00",
                 activebackground="black",variable=x,onvalue=1,offvalue=0,command=chech)
box1.place(x=300,y=260)




USERNAME=Entry(wid,font=("classic",10))

USERNAME.place(x=310,y=200)

PASSWORD=Entry(wid,font=("classic",10),show="*")
PASSWORD.place(x=310,y=230)

logibotton=Button(wid,text="Log in ",font=("Comic Sans",8,"bold"),
                  fg="red",bg="black",bd=3,relief=RAISED,command=user)

logibotton.place(x=356,y=290)

mu=Menu(wid,bg="black")
mu.config(background="black")
wid.config(menu=mu)
file=Menu(mu,tearoff=0)
mu.add_cascade(label="file",menu=file,)
file.add_command(label="who am I ?!!",command=who)
file.add_command(label="Exit" ,command=quit)





wid.mainloop()
