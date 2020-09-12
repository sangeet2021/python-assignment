from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from A.model.teacherr import  *
from A.back_end.connection import *

class teacher:
    def __init__(self,root):
        self.root=root
        self.root.title('Teacher Management System')
        self.root.geometry('1920x1080+0+0')

        title=Label(self.root,text='Teacher Management System',bd=10,relief=RIDGE,font=('arial',40,'bold'),bg='sky blue',fg='white')
        title.pack(side=TOP,fill=X)

        #all variable............
        self.Name_var=StringVar()
        self.ID_var=StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text= StringVar()

        self.dbconnect = DbConnection()





        #manage frame

        Manage_frame=Frame(self.root,bd=4,relief=GROOVE,bg='sky blue')
        Manage_frame.place(x=20,y=120,width=500,height=850)

        m_title=Label(Manage_frame,text='Manage Teachers',font=('arial',20,'bold'),bd=4, relief=GROOVE,bg='lavender')
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_name=Label(Manage_frame,text='Name:',font=('arial',15,'bold'),bd=4, relief=GROOVE,bg='lavender')
        lbl_name.grid(row=1,column=0,padx=20,pady=10,sticky='w')

        txt_name=Entry(Manage_frame,textvariable=self.Name_var,font=('arial',15,'bold'),bd=4, relief=GROOVE)
        txt_name.grid(row=1,column=1,padx=20,pady=10,sticky='w')

        lbl_roll = Label(Manage_frame, text='ID:', font=('arial', 15, 'bold'), bd=4, relief=GROOVE, bg='lavender')
        lbl_roll.grid(row=2, column=0, padx=20, pady=10, sticky='w')

        txt_roll = Entry(Manage_frame,textvariable=self.ID_var, font=('arial', 15, 'bold'), bd=4, relief=GROOVE)
        txt_roll.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        lbl_email = Label(Manage_frame, text='Email ID:', font=('arial', 15, 'bold'), bd=4, relief=GROOVE, bg='lavender')
        lbl_email.grid(row=3, column=0, padx=20, pady=10, sticky='w')

        txt_email = Entry(Manage_frame,textvariable=self.email_var, font=('arial', 15, 'bold'), bd=4, relief=GROOVE)
        txt_email.grid(row=3, column=1, padx=20, pady=10, sticky='w')

        lbl_gender = Label(Manage_frame, text='Gender:', font=('arial', 15, 'bold'), bd=4, relief=GROOVE,
                          bg='lavender')
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky='w')

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=('arial', 15, 'bold'),state='readonly',width=19)
        combo_gender['values']=('male','female','others')
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_frame, text='Contact:', font=('arial', 15, 'bold'), bd=4, relief=GROOVE,
                          bg='lavender')
        lbl_contact.grid(row=5, column=0, padx=20, pady=10, sticky='w')

        txt_contact = Entry(Manage_frame,textvariable=self.contact_var, font=('arial', 15, 'bold'), bd=4, relief=GROOVE)
        txt_contact.grid(row=5, column=1, padx=20, pady=10, sticky='w')

        lbl_dob = Label(Manage_frame, text='D.O. B:', font=('arial', 15, 'bold'), bd=4, relief=GROOVE,
                          bg='lavender')
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky='w')

        txt_dob = Entry(Manage_frame,textvariable=self.dob_var, font=('arial', 15, 'bold'), bd=4, relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=20, pady=10, sticky='w')


#button
        Btn_frame = Frame(Manage_frame,bd=1, relief=GROOVE, bg='sky blue')
        Btn_frame.place(x=10, y=550, width=450)

        Addbtn=Button(Btn_frame,text='Add',width=10,command=self.add).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(Btn_frame, text='Update', width=10,command=self.update).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(Btn_frame, text='Delete', width=10,command=self.delete).grid(row=0, column=2, padx=10, pady=10)
        Cleartn = Button(Btn_frame, text='Clear', width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



        #detail frame

        Detail_frame = Frame(self.root, bd=4, relief=GROOVE, bg='sky blue')
        Detail_frame.place(x=700, y=130, width=1200, height=850)

        lbl_search = Label(Detail_frame, text='Search By', font=('arial', 15, 'bold'), bd=4, relief=GROOVE,
                            bg='lavender')
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        combo_search = ttk.Combobox(Detail_frame,textvariable=self.search_by,width=10, font=('arial', 15, 'bold'), state='readonly')
        combo_search['values'] = ('Roll_no', 'Name', 'Contact')
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_frame,textvariable=self.search_text, width=15, font=('arial', 13, 'bold'), bd=4, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        Searchbtn = Button(Detail_frame, text='Search', width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        Clearbtn = Button(Detail_frame, text='Show All', width=10,command=self.fetch).grid(row=0, column=4, padx=10, pady=10)

        lbl_sort = Label(Detail_frame, text="Sort By:",bg ="lavender",fg='black',bd=4,relief=GROOVE, font=("arial", 13, "bold"), )
        lbl_sort.place(x=21, y=50,width =130)

        self.combo_sort = ttk.Combobox(Detail_frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.place(x=192, y=50)
        sortbtn = Button(Detail_frame, text="Sort", width=8, pady=1,
                         command=self.sort).place(x=400, y=50)


#table frame
        Table_frame = Frame(Detail_frame, bd=4, relief=GROOVE, bg='sky blue')
        Table_frame.place(x=10, y=90, width=1173, height=760)



        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.teacher_table=ttk.Treeview(Table_frame,columns=('Name','ID','Email','Gender',"Contact No.",'DOB'),xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)
        self.teacher_table.heading('Name',text='Name')
        self.teacher_table.heading('ID', text='ID')
        self.teacher_table.heading('Email', text='Email ID')
        self.teacher_table.heading('Gender', text='Gender')
        self.teacher_table.heading('Contact No.', text='Contact No.')
        self.teacher_table.heading('DOB', text='D.O.B')

        self.teacher_table['show']='headings'
        self.teacher_table.column('Name',width=163)
        self.teacher_table.column('ID', width=163)
        self.teacher_table.column('Email', width=163)
        self.teacher_table.column('Gender', width=163)
        self.teacher_table.column('Contact No.', width=163)
        self.teacher_table.column('DOB', width=163)

        self.teacher_table.pack(fill=BOTH,expand=1)
        self.teacher_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch()

    def get_cursor(self, ev):
            curosor_row = self.teacher_table.focus()
            contents = self.teacher_table.item(curosor_row)
            row = contents['values']

            self.Name_var.set(row[0])
            self.ID_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])



    def add(self):
        if self.Name_var.get()=="" or self.ID_var.get()=="" or self.email_var.get=="" or self.gender_var.get()=="" or \
                self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","incomplete value hala")

        else:
            teacher_obj=teacherr(self.Name_var.get(),self.ID_var.get(),self.email_var.get(),self.gender_var.get()
                           ,self.contact_var.get(),self.dob_var.get())
            query='insert into teacher values(%s,%s,%s,%s,%s,%s);'
            values=(teacher_obj.get_Name(),teacher_obj.get_ID(),teacher_obj.get_email(),teacher_obj.get_gender(),teacher_obj.get_contact(),teacher_obj.get_dob())
            self.dbconnect.insert(query,values)
            messagebox.showinfo('sucess','information inserted sucessfully')
            self.fetch()



    def fetch(self):
        query="select * from teacher"
        rows = self.dbconnect.select1(query)
        print(rows)
        if rows!=0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in rows:
                self.teacher_table.insert('',END,values=row)


    def search_data(self):
        query = " select * from teacher where Name = %s; "
        records = self.dbconnect.select2(query,(self.search_text.get(),))
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, str(self.search_text.get()))
        print(f"this is linear data{ans}")

        if ans:
            messagebox.showinfo('Success', 'congrats name exists in this list')
            query1 = "select * from teacher where Name=%s;"
            values1 = (ans,)
            records1 = self.dbconnect.select2(query1, values1)
            if len(records1) != 0:
                self.teacher_table.delete(*self.teacher_table.get_children())
                for row in records1:
                    self.teacher_table.insert('', END, values=row)


    @classmethod
    def linear_search(cls,data, item):
        for i in range(len(data)):
            if data[i] == item:
                return data[i]
        return False




    @classmethod
    def mergesort(cls, order, ascending=True):
        list = []
        if len(order) == 1:
            return order

        mit = len(order) // 2

        first_section = cls.mergesort(order[:mit])
        second_section = cls.mergesort(order[mit:])

        x = 0
        y = 0
        while x < len(first_section) and y < len(second_section):
            if first_section[x] > second_section[y]:
                list.append(second_section[y])
                y = y + 1

            else:
                list.append(first_section[x])
                x = x + 1

        conclusion = list + first_section[x:]
        conclusion = conclusion + second_section[y:]

        if ascending == True:
            return conclusion

        else:
            conclusion.reverse()
            return conclusion

    def sort(self):
        sortby = self.combo_sort.get()
        query = 'select * from teacher'
        value_fetch = self.dbconnect.select1(query)
        if sortby == 'Ascending':
            row = self.mergesort(value_fetch, True)


        elif sortby == 'Descending':
            row = self.mergesort(value_fetch, False)


        else:
            row = []

        if len(row) != 0:
            self.teacher_table.delete(
                *self.teacher_table.get_children())
            for rows in row:
                self.teacher_table.insert('', END, values=rows)

    def update(self):
        teacher_obj=teacherr(self.Name_var.get(),self.ID_var.get(),self.email_var.get(),self.gender_var.get()
                       ,self.contact_var.get(),self.dob_var.get())
        query='update teacher set  ID=%s, email=%s, gender=%s, contact=%s, dob=%s where Name=%s;'
        Name=self.Name_var.get()
        ID=self.ID_var.get()
        email=self.email_var.get()
        gender=self.gender_var.get()
        contact=self.contact_var.get()

        dob=self.dob_var.get()
        values=(ID,gender,contact,email,gender,Name)
        self.dbconnect.update(query,values)
        messagebox.showinfo('sucess', 'data updated sucessfully')
        self.fetch()

    def clear(self):
        self.Name_var.set("")
        self.ID_var.set("")

        self.gender_var.set("")
        self.contact_var.set("")
        self.email_var.set("")
        self.dob_var.set("")
        messagebox.showinfo("success","values cleared")


    def delete(self):
        query = "delete from teacher where Name=%s;"
        id = self.Name_var.get()
        value = (id,)
        self.dbconnect.delete(query, value)
        messagebox.showinfo("Success", "Data deleted successfully")
        self.fetch()


    def exit(self):
        self.root.destroy()




#
#root=Tk()
#ob=teacher(root)
#root.mainloop()