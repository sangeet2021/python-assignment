from tkinter import *
from tkinter import messagebox
from A.front_end.welcome import *

class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title('Login Page')
        self.root.geometry('1920x1080+0+0')

        #variables
        self.uname=StringVar()
        self.pass_=StringVar()




        title=Label(self.root,text="login System",font=('arial',40,'bold'),bd=4, relief=GROOVE,bg='lavender',fg='purple')
        title.place(x=0,y=0,relwidth=1)

        login_frame=Frame(self.root,bg='pink')
        login_frame.place(x=550,y=400)

        lbluser=Label(login_frame,text='Username',font=('arial',20,'bold'))
        lbluser.grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(login_frame,bd=5,textvariable=self.uname,relief=RIDGE,font=('',15))
        txtuser.grid(row=1,column=1,padx=20,pady=20)

        lblpass=Label(login_frame,text='Password',font=('arial',20,'bold'))
        lblpass.grid(row=2,column=0,padx=20,pady=10)
        txtpass = Entry(login_frame, bd=5, textvariable=self.pass_,relief=RIDGE, font=('', 15))
        txtpass.grid(row=2, column=1, padx=20, pady=20)

        btn_login=Button(login_frame,text='Login',width=15,command=self.login,font=('arial',14,'bold'),bg='purple',fg='lavender')
        btn_login.grid(row=3,column=2,padx=20,pady=20)

    def login(self):
        if self.uname.get()=='' and self.pass_.get()=='':
            messagebox.showerror('Error',"Fill all fields")
        elif self.uname.get()=='1'or self.pass_.get()=='1':
             self.root.withdraw()
             root = Toplevel()
             A.front_end.welcome.welcome(root)

             messagebox.showinfo('Success',f'welcome{self.uname.get()}')


        else:
            messagebox.showerror('Error','Invalid Usrname or Password')





root=Tk()
obj=login_system(root)
root.mainloop()