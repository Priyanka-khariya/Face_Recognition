from importlib.resources import contents
from logging import root
from re import L
from tkinter import*
from tkinter import ttk
from tkinter import dialog
from PIL import Image,ImageTk
from pyrsistent import v
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import csv
from tkinter import filedialog 
from time import strftime
from datetime import datetime

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        #-----------Variables-------------------
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attend=StringVar()
        

        #bg image
        img3=Image.open(r"C:\Users\karan\face recognition\FR\Images\bg.jpg")
        img3=img3.resize((1530,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=810)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white", fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=150,width=1480,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\karan\face recognition\FR\Images\download.jpg")
        img_left=img_left.resize((720,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=150)
     
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=5,y=135,width=720,height=400)

        #label and entry

        #attendance ID

        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame, textvariable=self.var_attend_id, width=20, font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx =10,pady=5,sticky=W)

        #student roll l

        student_roll_label = Label(left_inside_frame,text="Roll.No:",font=("times new roman",13,"bold"),bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_roll,width=15,font=("times new roman",13,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Student Name
        student_name_label = Label(left_inside_frame,text="Std-Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=15,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    

        #time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=15,font=("times new roman",13,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=15,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_inside_frame,text="Attend-status:",font=("times new roman",13,"bold"),bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attend,width=13,font=("times new roman",13,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        #button Frame 
        btn_frame =Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        upadate_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        upadate_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)        

        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=("times new roman ",12,"bold"))
        Right_frame.place(x=750,y=10,width=720 ,height=580)


        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=2,y=2,width=710 ,height=548)

        #===scroll====
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

#         self.AttendanceReport=ttk.Treeview(table_frame,column=("id","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_x.config(command=self.AttendanceReport.xview)
#         scroll_y.config(command=self.AttendanceReport.yview)


        #create table 
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","time","date","attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attend",text="Attendance")
        self.AttendanceReportTable["show"]="headings"


        # Set Width of Colums 
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attend",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        
# =========================Fetch Data Import data ===============

    def fetchData(self,rows):
            # global mydata
            # mydata = rows
         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
         for i in rows:
           self.AttendanceReportTable.insert("",END,values=i)
                # print(i)
            
#import csv
    def importCsv(self):
         global mydata
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
         with open(fln) as myfile:
           csvread=csv.reader(myfile,delimiter=",")
           for i in csvread:
             mydata.append(i)
           self.fetchData(mydata)

    #==================Export CSV=============
    def exportCsv(self):
        try:
           if len(mydata)<1:
             messagebox.showerror("Error","No Data Found!",parent=self.root)
             return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
           with open(fln,mode="w",newline="") as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
               exp_write.writerow(i)
             messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                   messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)   

    def get_cursor(self,rows):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_attend_id.set(rows[0])
            self.var_attend_roll.set(rows[1])
            self.var_attend_name.set(rows[2])
            self.var_attend_time.set(rows[3])
            self.var_attend_date.set(rows[4])
            self.var_attend_attend.set(rows[5])
    def reset_data(self):
            self.var_attend_id.set("")
            self.var_attend_roll.set("")
            self.var_attend_name.set("")
            self.var_attend_time.set("")
            self.var_attend_date.set("")
            self.var_attend_attend.set("")

        

if __name__ == "__main__":
      root=Tk()
      obj=Attendance(root)
      root.mainloop()         