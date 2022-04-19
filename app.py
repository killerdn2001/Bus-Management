import sys
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
app = Tk()
app.title("Assignment 2")
app.geometry("900x800+400+10")
app.config(bg='dark slate gray')
img1 = Image.open("logo.png")
img1 = img1.resize((100, 100))
img1 = ImageTk.PhotoImage(img1)
exit1 = 0
func = 0
mydb = 0
# Label(image=img1, bg='dark slate gray').place(relx=0.5, y=150, anchor=CENTER)
# mydb=mysql.connector.connect(
# 	user='',
# 	password='1',
# 	host="127.0.0.1",
# 	database='assignment'
# )


class cus_info():
    global exit1
    # def __init__(self):

    def find(self):
        if len(self.e1.get()) != 8 or self.e1.get()[0:2] != 'KH':
            messagebox.showerror('Error', 'Hãy nhập đúng cú pháp!')
            return
        c = mydb.cursor()
        sql1 = "select * from `hành khách` where `Mã hành khách`=%s"
        value = [self.e1.get()]
        c.execute(sql1, value)
        rec = c.fetchall()
        if len(rec) == 0:
            messagebox.showinfo(
                'Not found', 'Không tìm thấy hành khách có mã vừa nhập!')
            return
        style.configure("Treeview", background="silver", foreground="black")
        style.map('Treeview', background=[('selected', 'dim gray')])
        treev = ttk.Treeview(self.framea, selectmode='browse')
        treev.place(x=40, y=410, height=60)
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Defining heading
        treev['show'] = 'headings'
        treev.column("1", width=90, anchor='c')
        treev.column("2", width=85, anchor='c')
        treev.column("3", width=77, anchor='c')
        treev.column("4", width=77, anchor='c')
        treev.column("5", width=77, anchor='c')
        treev.column("6", width=180, anchor='c')
        treev.column("7", width=110, anchor='c')
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="Mã hành khách")
        treev.heading("2", text="CMND/CCCD")
        treev.heading("3", text="Điện thoại")
        treev.heading("4", text="Nghề")
        treev.heading("5", text="Giới tính")
        treev.heading("6", text="Email")
        treev.heading("7", text="Ngày sinh")
        treev.insert("", 'end',
                     values=rec[0], tag=('odd',))
        treev.tag_configure('odd', background='bisque')

    def exc(self):
        global func
        func = 1
        exit1.place(relx=0.90, rely=0.95, anchor=NW)
        self.framea = Frame(app, bg='dark slate gray')
        self.framea.place(x=50, y=220, width=800, height=455)
        self.func_a = Label(self.framea, text='XEM THÔNG TIN HÀNH KHÁCH',
                            bg='dark slate gray', fg='orange', font=('Arial', 20, 'bold'))
        self.func_a.place(relx=0.5, y=20, anchor=CENTER)
        c = mydb.cursor()
        c.execute("select * from `hành khách`")
        rec = c.fetchall()
        style.configure("Treeview", background="silver", foreground="black")
        style.map('Treeview', background=[('selected', 'dim gray')])
        treev = ttk.Treeview(self.framea, selectmode='browse')
        treev.place(x=40, y=60, height=280)
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = Scrollbar(self.framea, command=treev.yview)
        verscrlbar.place(x=727, y=60, height=280)
        Label(self.framea, text='Tìm hành khách có mã:', bg='dark slate gray',
              fg='orange', font=('Arial', 10, 'bold')).place(x=90, y=350)
        Label(self.framea, text='(Cú pháp: KH[0-9][0-9][0-9][0-9][0-9][0-9)',
              bg='dark slate gray', fg='orange', font=('Arial', 10)).place(x=250, y=350)
        self.b1 = Button(self.framea, text='Tìm', bg='orange3', font=('Arial', 8, 'bold'),
                         bd=4, command=lambda: self.find()).place(relx=0.5, y=390, anchor=CENTER, width=100)
        self.e1 = Entry(self.framea)
        self.e1.place(x=510, y=350, width=150)
        treev.configure(yscrollcommand=verscrlbar.set)
        # Defining number of columns
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        # Defining heading
        treev['show'] = 'headings'
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=90, anchor='c')
        treev.column("2", width=85, anchor='c')
        treev.column("3", width=77, anchor='c')
        treev.column("4", width=77, anchor='c')
        treev.column("5", width=77, anchor='c')
        treev.column("6", width=180, anchor='c')
        treev.column("7", width=110, anchor='c')
        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="Mã hành khách")
        treev.heading("2", text="CMND/CCCD")
        treev.heading("3", text="Điện thoại")
        treev.heading("4", text="Nghề")
        treev.heading("5", text="Giới tính")
        treev.heading("6", text="Email")
        treev.heading("7", text="Ngày sinh")
        i = 0
        for re in rec:
            if i % 2 == 0:
                treev.insert("", 'end',
                             values=re, tag=('odd',))
            else:
                treev.insert("", 'end',
                             values=re, tag=('even',))
            i += 1
        treev.tag_configure('odd', background='bisque')
        treev.tag_configure('even', background='gainsboro')
        c.close()

    def exit(self):
        global func
        if func == 1:
            self.framea.destroy()
            exit1.place_forget()

# Thêm một tuyến tàu xe


class add_route():
    global exit1

    def check_complete(self):
        for tri in self.trip:
            for t in tri:
                if t.get() == '':
                    messagebox.showerror('Error', 'Hãy nhập đủ lịch trình!')
                    return
        if (self.vehicle.get() == 'Xe Bus' and self.e1.get()[0] != 'B' or
                self.vehicle.get() == 'Tàu điện' and self.e1.get()[0] != 'T' or
                len(self.e1.get()) != 4 or (self.e1.get())[1:4].isnumeric() == 0):
            messagebox.showerror(
                'Error', 'Hãy nhập đúng cú pháp cho Mã tuyến tàu/xe!')
            return
        if self.vehicle.get() == 'Tàu điện':
            if len(self.e2.get()) != 1 or self.e2.get().isnumeric():
                messagebox.showerror(
                    'Error', 'Hãy nhập đúng cú pháp cho Mã tuyến tàu!')
                return
            if self.e4.get().isnumeric() == 0:
                messagebox.showerror(
                    'Error', 'Hãy nhập đúng cú pháp cho Đơn giá!')
                return
        c = mydb.cursor()
        id_list = []
        for des in self.des_list:
            sql1 = "SELECT `Mã ga/trạm` FROM `Ga trạm` where `Tên`=%s"
            value = [des.get()]
            c.execute(sql1, value)
            result = c.fetchall()
            id_list.append(result)
        sql1 = "INSERT INTO `Chuyến tàu/xe ghé ga/trạm`(`Mã tuyến`,STT,`Mã ga/trạm`,`STT dừng`,`Giờ ghé`,`Giờ đi`) values (%s,%s,%s,%s,%s,%s)"
        vals1 = []
        for j in range(int(self.e5.get())):
            for k in range(self.i):
                come = ''
                leave = ''
                t = 0
                for tri in self.trip[j][k].get():
                    if tri == '/':
                        t = 1
                        continue
                    if t == 0:
                        come += tri
                    else:
                        leave += tri
                if t == 0 or leave == '' and k < self.i-1:
                    messagebox.showerror(
                        'Error', 'Hãy nhập đúng cú pháp cho lịch trình!')
                    return
                if leave == '' and k == self.i-1:
                    leave = None
                vals1.append(
                    (self.e1.get(), j+1, id_list[k][0][0], k+1, come, leave))
        sql = "INSERT INTO `tuyến tàu xe` values (%s)"
        val = [self.e1.get()]
        c.execute(sql, val)
        if self.vehicle.get() == 'Xe Bus':
            sql = "INSERT INTO `tuyến xe bus`(`Mã tuyến tàu/xe`) values (%s)"
        else:
            sql = "INSERT INTO `tuyến tàu điện`(`Mã tuyến tàu/xe`,`Mã tuyến tàu`,`Tên tuyến tàu`,`Đơn giá`) values (%s,%s,%s,%s)"
            val = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()]
        c.execute(sql, val)
        sql = "INSERT INTO `Chuyến tàu/xe`(`Mã tuyến`,STT) values (%s,%s)"
        vals = []
        for j in range(int(self.e5.get())):
            # val=(self.e1.get(),j+1)
            vals.append((self.e1.get(), j+1))
        c.executemany(sql, vals)
        c.executemany(sql1, vals1)
        mydb.commit()
        messagebox.showinfo('Success', 'Bạn đã nhập một tuyến tàu xe')
        self.frameb.destroy()

    def input_sched(self):
        if self.e5.get() == '':
            messagebox.showerror('Error', 'Hãy nhập số chuyến!')
            return
        wid = (self.frameb.winfo_width()-63)/(self.i)
        x0 = 63
        y3 = self.y1+self.fr.winfo_height()+70
        Label(self.frameb, text='(Cú pháp nhập: Giờ ghé/Giờ đi)',
              bg='dark slate gray', fg='orange',).place(x=0, y=y3)
        y3 += 20
        for k1 in range(self.i):
            Label(self.frameb, text='Trạm '+self.des_list[k1].get(
            ), bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold')).place(x=x0, y=y3, width=wid)
            x0 += wid+2
        y3 += 20
        for j in range(int(self.e5.get())):
            x2 = 63
            tri = []
            Label(self.frameb, text='Chuyến '+str(j+1), bg='dark slate gray',
                  fg='orange', font=('Arial', 10, 'bold')).place(x=0, y=y3, width=63)
            for k in range(self.i):
                tri_entry = Entry(self.frameb)
                tri.append(tri_entry)
                if k == self.i-1:
                    tri_entry.place(x=x2, y=y3, width=wid-5)
                else:
                    tri_entry.place(x=x2, y=y3, width=wid)
                x2 += wid
            y3 += 20
            self.trip.append(tri)
        Button(self.frameb, text='Hoàn tất', bg='orange3', font=('Arial', 8, 'bold'), bd=4,
               command=lambda: self.check_complete()).place(relx=0.5, rely=0.9, anchor=CENTER)

    def add_des(self, event):
        self.h += 20
        self.fr.place(x=0, y=self.y1, height=self.h,
                      width=self.frameb.winfo_width())
        self.lb5.place(x=0, y=self.y1+self.fr.winfo_height()+30)
        self.confirm.place(relx=0.5, y=self.y1 +
                           self.fr.winfo_height()+70, anchor=CENTER)
        self.e5.place(x=self.x1, y=self.y1 +
                      self.fr.winfo_height()+30, width=130)
        self.i += 1
        self.y2 += 20
        Label(self.fr, text='Điểm dừng '+str(self.i)+':', bg='dark slate gray',
              fg='orange', font=('Arial', 10, 'bold')).place(x=0, y=self.y2)
        self.des_box = ttk.Combobox(self.fr, state='readonly')
        self.des_box['values'] = self.rec
        self.des_box.place(x=self.x1, y=self.y2, width=130)
        self.des_list.append(self.des_box)
        self.des_but.place_forget()
        self.des_box.bind('<<ComboboxSelected>>', lambda event,
                          j=self.i-1: self.change_state(event, j))
        self.change_state(event, self.i-1)
        self.des_but.place(relx=0.5, y=self.y2+38, anchor=CENTER)

    def change_state(self, event, j):
        if self.des_but['state'] == DISABLED:
            self.des_but['state'] = NORMAL
        elif self.des_list[j].get() == '':
            self.des_but['state'] = DISABLED

    def input_des(self):
        if self.e1.get() == '':
            messagebox.showerror('Error', 'Hãy nhập đủ thông tin!')
            return
        if self.vehicle.get() == 'Tàu điện' and (self.e2.get() == '' or self.e3.get() == '' or self.e4.get() == ''):
            messagebox.showerror('Error', 'Hãy nhập đủ thông tin')
            return
        else:
            self.l.place_forget()
            self.y2 = 0
            self.h = 70
            self.fr.place(x=0, y=self.y1, height=self.h,
                          width=self.frameb.winfo_width())
            Label(self.fr, text='Điểm dừng '+str(self.i)+':', bg='dark slate gray',
                  fg='orange', font=('Arial', 10, 'bold')).place(x=0, y=0)
            c = mydb.cursor()
            if self.vehicle.get() == 'Xe Bus':
                c.execute(
                    "select Tên from `Ga trạm` where `Mã ga/trạm` LIKE %s  order by Tên", ('B'+"%",))
            else:
                c.execute(
                    "select Tên from `Ga trạm` where `Mã ga/trạm` LIKE %s  order by Tên", ('T'+"%",))
            self.rec = c.fetchall()
            self.des_box = ttk.Combobox(self.fr, state='readonly')
            self.des_box['values'] = self.rec
            self.des_box.place(x=self.x1, y=0, width=130)
            self.des_list.append(self.des_box)
            self.des_but = Button(self.fr, text='Thêm trạm', bg='orange3', bd=4, font=(
                'Arial', 8, 'bold'), state=DISABLED)
            self.des_but.bind('<Button-1>', self.add_des)
            self.des_box.bind('<<ComboboxSelected>>', lambda event,
                              j=self.i-1: self.change_state(event, j))
            self.des_but.place(relx=0.5, y=38, anchor=CENTER)

    def selected(self, event):
        self.y1 = self.y+30
        self.lb1.place(x=0, y=self.y1)
        self.e1.place(x=self.x1, y=self.y1, width=130)
        self.y1 += 30
        if self.vehicle.get() == 'Tàu điện':
            Label(self.frameb, text='(Cú pháp: T[0-9][0-9][0-9])',
                  bg='dark slate gray', fg='orange').place(x=150, y=self.y1-30)
            self.lb2.place(x=0, y=self.y1)
            self.e2.place(x=self.x1, y=self.y1, width=130)
            self.lb6.place(x=130, y=self.y1)
            self.y1 += 30
            self.lb3.place(x=0, y=self.y1)
            self.e3.place(x=self.x1, y=self.y1, width=130)
            self.y1 += 30
            self.lb4.place(x=0, y=self.y1)
            self.e4.place(x=self.x1, y=self.y1, width=130)
            self.y1 += 30
            self.l.place(relx=0.5, y=self.y1+10, anchor=CENTER)
        elif self.vehicle.get() == 'Xe Bus':
            Label(self.frameb, text='(Cú pháp: B[0-9][0-9][0-9])',
                  bg='dark slate gray', fg='orange').place(x=150, y=self.y1-30)
            self.y1 = self.y+60
            self.l.place_forget()
            self.lb2.place_forget()
            self.lb3.place_forget()
            self.lb4.place_forget()
            self.lb6.place_forget()
            self.e2.place_forget()
            self.e3.place_forget()
            self.e4.place_forget()
            self.l.place(relx=0.5, y=self.y1+10, anchor=CENTER)

    def exc(self):
        global func
        func = 2
        self.frameb = Frame(app, bg='dark slate gray')
        self.frameb.place(relx=0.5, rely=0.6, anchor=CENTER,
                          width=500, height=550)
        self.func_b = Label(self.frameb, text='THÊM TUYẾN TÀU XE',
                            bg='dark slate gray', fg='orange', font=('Arial', 20, 'bold'))
        self.func_b.place(relx=0.5, y=20, anchor=CENTER)
        exit1.place(relx=0.90, rely=0.95, anchor=NW)
        self.des_list = []
        self.lb = Label(self.frameb, text='Chọn loại phương tiện cần thêm:',
                        fg='orange', bg='dark slate gray', font=('Arial', 10, 'bold'))
        self.vehicle = ttk.Combobox(self.frameb, state='readonly')
        self.vehicle['values'] = ('Xe Bus', 'Tàu điện')
        self.lb.place(x=0, y=50)
        app.update()
        self.x1 = self.lb.winfo_width()+120
        self.y = 50
        self.vehicle.place(x=self.x1, y=self.y, width=130)
        self.lb1 = Label(self.frameb, text='Nhập mã tuyến tàu/xe:',
                         bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.lb2 = Label(self.frameb, text='Nhập mã tuyến tàu:',
                         bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.lb3 = Label(self.frameb, text='Nhập tên tuyến tàu:',
                         bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.lb4 = Label(self.frameb, text='Nhập đơn giá:',
                         bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.lb6 = Label(self.frameb, text='(Cú pháp: 1 chữ cái)',
                         bg='dark slate gray', fg='orange')
        self.e1 = Entry(self.frameb)
        self.e2 = Entry(self.frameb)
        self.e3 = Entry(self.frameb)
        self.e4 = Entry(self.frameb)
        self.l = Button(self.frameb, text='Nhập lộ trình', bg='orange3', bd=4, font=(
            'Arial', 8, 'bold'), command=lambda: self.input_des())
        self.i = 1
        self.vehicle.bind('<<ComboboxSelected>>', self.selected)
        self.fr = LabelFrame(self.frameb, text='Lộ trình',
                             bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.lb5 = Label(self.frameb, text='Nhập số chuyến',
                         bg='dark slate gray', fg='orange', font=('Arial', 10, 'bold'))
        self.e5 = Entry(self.frameb)
        self.confirm = Button(self.frameb, text='Nhập lịch trình', bg='orange3', bd=4, font=(
            'Arial', 8, 'bold'), command=lambda: self.input_sched())
        self.trip = []

    def exit(self):
        global func
        if func == 2:
            res = messagebox.askquestion(
                'Cảnh báo', 'Quay lại và hủy bỏ quá trình thêm tuyến tàu/xe?')
            if res == 'yes':
                self.frameb.destroy()
                exit1.place_forget()
# img = Image.open("cap.jpg")
# img = img.resize((700, 700))
# img = ImageTk.PhotoImage(img)
# Label(image=img).place(x=0,y=0)


class static():
    # def __init__(self):
    global exit1

    def confirm(self):

        try:
            cursor = mydb.cursor()
            cursor.callproc('ThongKeLuotNguoi', [
                self.id_box.get(), self.e2.get(), self.e3.get()])
            style.configure("Treeview", background="silver",
                            foreground="black")
            style.map('Treeview', background=[('selected', 'dim gray')])
            treev = ttk.Treeview(self.framec, selectmode='browse')
        # Calling pack method w.r.to treeview
            treev.place(relx=0.5, rely=0.5, anchor=CENTER, height=200)
        # Constructing vertical scrollbar
        # with treeview
            verscrlbar = Scrollbar(self.framec, command=treev.yview)
            verscrlbar.place(x=400, rely=0.5, anchor=CENTER, height=200)
        # Configuring treeview
            treev.configure(yscrollcommand=verscrlbar.set)
        # Defining number of columns
            treev["columns"] = ("1", "2")
        # Defining heading
            treev['show'] = 'headings'
        # Assigning the width and anchor to  the
        # respective columns
            treev.column("1", width=170, anchor='c')
            treev.column("2", width=170, anchor='c')
        # Assigning the heading names to the
        # respective columns
            treev.heading("1", text="Ngày")
            treev.heading("2", text="Tổng số lượt người")

            for result in cursor.stored_results():
                print(result.fetchall())
                i = 0
                for r in result.fetchall():

                    if i % 2 == 0:
                        treev.insert("", 'end',
                                     values=(r[0], r[1]), tag=('odd',))
                    else:
                        treev.insert("", 'end',
                                     values=(r[0], r[1]), tag=('even',))
                    i += 1
            treev.tag_configure('odd', background='bisque')
            treev.tag_configure('even', background='gainsboro')
        except mysql.connector.Error as e:

            print(e.msg)
            messagebox.showerror('Error', 'Ngày bắt đầu phải nhỏ hơn kết thúc')
            self.exc()

    def exc(self):
        global func
        func = 3
        self.framec = Frame(app, bg='dark slate gray')
        self.framec.place(relx=0.5, rely=0.6, anchor=CENTER,
                          width=450, height=550)
        self.func_c = Label(self.framec, text='THỐNG KÊ LƯỢT NGƯỜI',
                            bg='dark slate gray', fg='orange', font=('Arial', 20, 'bold'))
        self.func_c.place(relx=0.5, y=30, anchor=CENTER)
        exit1.place(relx=0.90, rely=0.95, anchor=NW)
        Label(self.framec, text='Chọn mã tuyến:', bg='dark slate gray',
              fg='orange', font=('Arial', 10, 'bold')).place(x=70, y=80)
        Label(self.framec, text='Nhập ngày bắt đầu:', bg='dark slate gray',
              fg='orange', font=('Arial', 10, 'bold')).place(x=70, y=110)
        Label(self.framec, text='Nhập ngày kết thúc:', bg='dark slate gray',
              fg='orange', font=('Arial', 10, 'bold')).place(x=70, y=140)
        c = mydb.cursor()
        c.execute("select `Mã tuyến` from `tuyến tàu xe`")
        rec = c.fetchall()
        self.id_box = ttk.Combobox(self.framec, state='readonly')
        self.id_box['values'] = rec
        self.id_box.place(x=260, y=80, width=130)
        self.e2 = Entry(self.framec)
        self.e2.place(x=260, y=110, width=130)
        self.e3 = Entry(self.framec)
        self.e3.place(x=260, y=140, width=130)
        Button(self.framec, text='Xác nhận', bg='orange3', bd=4, font=(
            'Arial', 8, 'bold'), command=lambda: self.confirm()).place(relx=0.5, y=190, anchor=CENTER)

    def exit(self):
        global func
        if func == 3:
            self.framec.destroy()
            exit1.place_forget()


style = ttk.Style()
# main_fr=Frame(app,bg='gold')
# main_fr.place(relx=0.5,rely=0.5,anchor=CENTER,height=350,width=350)
main_lb = Label(text='MENU', fg='green2', bg='dark slate gray',
                font=('Arial', 25, 'bold'))
# main_lb.place(relx=0.5,rely=0.35,anchor=CENTER)


def log():
    global mydb
    mydb = mysql.connector.connect(
        user='sManager',
        password='1',
        host="127.0.0.1",
        database='assignment')
    global exit1
    A = cus_info()
    but1 = Button(text='Xem thông tin hành khách', font=('Arial', 16, 'bold'),
                  bg='orange3', bd=7, command=lambda: [A.exc(), B.exit(), C.exit()])
    but1.place(relx=0.5, rely=0.45, anchor=CENTER)
    B = add_route()
    app.update()
    but2 = Button(text='Thêm một tuyến tàu xe', font=('Arial', 16, 'bold'),
                  bg='orange3', bd=7, command=lambda: [B.exc(), A.exit(), C.exit()])
    but2.place(relx=0.5, y=410, anchor=CENTER, width=but1.winfo_width())
    C = static()
    but3 = Button(text='Thống kê lượt người', font=('Arial', 16, 'bold'),
                  bg='orange3', bd=7, command=lambda: [C.exc(), A.exit(), B.exit()])
    but3.place(relx=0.5, y=460, anchor=CENTER, width=but1.winfo_width())
    exit1 = Button(text='Quay lại', bg='orange3', bd=4, font=(
        'Arial', 8, 'bold'), command=lambda: [A.exit(), B.exit(), C.exit()])
    # app.mainloop()


class login:
    def log_out(self):
        self.b_out.place_forget()
        self.log_in()

    def check_log(self):
        if self.e1.get() == '' or self.e2.get() == '':
            messagebox.showerror('Error', 'Hãy nhập đủ thông tin!')
            return
        if self.e1.get() != 'sManager':
            messagebox.showerror('Error', 'Sai Username!')
            return
        if self.e2.get() != '1':
            messagebox.showerror('Error', 'Sai Password!')
            return
        global mydb
        mydb = mysql.connector.connect(
            user='sManager',
            password='1',
            host="127.0.0.1",
            database='assignment'
        )
        self.framelog.place_forget()
        log()

        self.b_out.place(relx=0.5, y=508, anchor=CENTER, width=296)

    def log_in(self):
        self.framelog = Frame(app, bg='dark slate gray')
        self.framelog.place(x=50, y=200, width=800, height=560)
        Label(self.framelog, text='WELCOME', bg='dark slate gray', fg='orange', font=(
            'Arial', 25, 'bold')).place(relx=0.5, y=50, anchor=CENTER)
        Label(self.framelog, text='LOGIN TO USE', bg='dark slate gray', fg='orange', font=(
            'Arial', 17, 'bold')).place(relx=0.5, y=120, anchor=CENTER)
        Label(self.framelog, text='Username:', bg='dark slate gray',
              fg='orange', font=('Arial', 13, 'bold')).place(x=240, y=230)
        Label(self.framelog, text='Password:', bg='dark slate gray',
              fg='orange', font=('Arial', 13, 'bold')).place(x=240, y=260)
        self.e1 = Entry(self.framelog)
        self.e1.place(x=390, y=230, width=150)
        self.e2 = Entry(self.framelog, show='*')
        self.e2.place(x=390, y=260, width=150)
        Button(self.framelog, text='Đăng nhập', bg='orange3', bd=4, font=(
            'Arial', 8, 'bold'), command=lambda: self.check_log()).place(relx=0.5, y=320, anchor=CENTER)
        self.b_out = Button(app, text='Đăng xuất', bg='orange3', font=(
            'Arial', 16, 'bold'), bd=7, command=lambda: self.log_out())


def props(cls):
    return [i for i in cls.__dict__.keys()]


# login().log_in()
log()
app.mainloop()
