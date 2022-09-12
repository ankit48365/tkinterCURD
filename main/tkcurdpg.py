


import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
from tkinter import *

server = 'ak-az-sqlserver.database.windows.net'
database = 'ak-az-sqlserver'
username = 'admin4'
password = '{P@ssword2021}'   
driver= '{ODBC Driver 17 for SQL Server}'
connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['STATION_NAME'])
    e2.insert(0,select['LATITUDE'])
    e3.insert(0,select['LONGITUDES'])
    e4.insert(0,select['REMARK'])
 
 
def Add():
    StaName = e1.get()
    LAT = e2.get()
    LONG = e3.get()
    REMARK = e4.get()
 
    mssqldb=pyodbc.connect(connectionString)
    mycursor=mssqldb.cursor()
 
    try:
    #    sql = "INSERT INTO  PROJ5.SITE_TBL (STATION_NAME,LATITUDE,LONGITUDES,REMARK) VALUES (?, ?, ?, ?)"
       sql = "INSERT INTO  PROJ5.SITE_TBL (STATION_NAME,LATITUDE,LONGITUDES,REMARK) VALUES (?,?,?,?)"

       val = (StaName,LAT,LONG,REMARK)
       mycursor.execute(sql, val)
       mssqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Employee inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mssqldb.rollback()
       mssqldb.close()
 
 
def update():
    StaName = e1.get()
    LAT = e2.get()
    LONG = e3.get()
    REMARK = e4.get()
    mssqldb=pyodbc.connect(connectionString)
    mycursor=mssqldb.cursor()
 
    try:
       sql = "Update  PROJ5.SITE_TBL set LATITUDE= ?,LONGITUDES= ?,REMARK= ? where STATION_NAME= ?"
       val = (LAT,LONG,REMARK,StaName)
       mycursor.execute(sql, val)
       mssqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mssqldb.rollback()
       mssqldb.close()
 
def delete():
    StaName = e1.get()
 
    mssqldb=pyodbc.connect(connectionString)
    mycursor=mssqldb.cursor()
 
    try:
       sql = "delete from PROJ5.SITE_TBL where STATION_NAME = ?"
       val = (StaName,)
       mycursor.execute(sql, val)
       mssqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mssqldb.rollback()
       mssqldb.close()



def show():

   server = 'ak-az-sqlserver.database.windows.net'
   database = 'ak-az-sqlserver'
   username = 'admin4'
   password = '{P@ssword2021}'   
   driver= '{ODBC Driver 17 for SQL Server}'
   connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'
   
   mssqldb = pyodbc.connect(connectionString)
   mycursor = mssqldb.cursor()
   mycursor.execute("SELECT STATION_NAME,LATITUDE,LONGITUDES,REMARK FROM PROJ5.SITE_TBL")
   records = mycursor.fetchall()
#    print(records)

   for i, (staName, LAT, LONG, REMARK) in enumerate(records, start=1):
      listBox.insert("", "end", values=(staName, LAT, LONG, REMARK))
    #   mssqldb.close()
 
root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
 
tk.Label(root, text="Location Details", fg="black", font=(None, 20)).place(x=300, y=5)
 
tk.Label(root, text="STATION_NAME").place(x=10, y=10)
Label(root, text="LATITUDE").place(x=10, y=40)
Label(root, text="LONGITUDES").place(x=10, y=70)
Label(root, text="REMARK").place(x=10, y=100)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)
 
Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
 
cols = ('STATION_NAME', 'LATITUDE', 'LONGITUDES','REMARK')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()