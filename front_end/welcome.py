from tkinter import *
import A.front_end.student
import A.front_end.teacher
from PIL import ImageTk, Image


class welcome:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to School Management System')
        self.wn.geometry('1920x1080+0+0')




        self.lb_heading = Label(self.wn, text='Welcome', bg='lavender', fg="purple",
                                font=('arial', 20, 'bold'))
        self.lb_heading.place(x=0, y=0, relwidth=1)





        # Button
        self.btn_wep = Button(self.wn, text='Student Management System', fg='purple', bg='lavender', font=('arial', 14, 'bold'), bd='6',
                              command=self.btn_student_click)
        self.btn_wep.place(x=753, y=400,)

        self.btn_arm = Button(self.wn, text='Teacher Management System', fg='purple', bg='lavender', font=('arial', 14, 'bold'), bd='6',
                              command=self.btn_teacher_click)
        self.btn_arm.place(x=750, y=500,)


        self.btn_exit = Button(self.wn, text='Exit', fg='purple', bg='lavender', font=('arial', 14, 'bold'), bd='6',
                               command=self.btn_exit_click)
        self.btn_exit.place(x=880, y=600)

    #


    def btn_student_click(self):
        user_window = Toplevel()
        A.front_end.student.student(user_window)


    def btn_teacher_click(self):
        user_window = Toplevel()
        A.front_end.teacher.teacher(user_window)




    def btn_exit_click(self):
        self.wn.destroy()

#wn=Tk()

#welcome(wn)
#wn.mainloop()
