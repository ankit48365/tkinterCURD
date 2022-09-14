
def func_Main():

   import tkinter as tk
   from tkinter import ttk, messagebox, Tk
   import pyodbc
   # from tkinter import *

   server = 'ak-az-sqlserver.database.windows.net'
   database = 'ak-az-sqlserver'
   username = 'admin4'
   password = '{P@ssword2021}'   
   driver= '{ODBC Driver 17 for SQL Server}'
   connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'


   def GetValue(event):
      e1.delete(0, tk.END)
      e2.delete(0, tk.END)
      e3.delete(0, tk.END)
      e4.delete(0, tk.END)
      e5.delete(0, tk.END)
      # e6.delete(0, tk.END)
      # e7.delete(0, tk.END)
      e8.delete(0, tk.END)


      row_id = listBox.selection()[0]
      select = listBox.set(row_id)
      e1.insert(0,select['FK_STATION_NAME'])
      e2.insert(0,select['IPSEC'])
      e3.insert(0,select['ACL'])
      e4.insert(0,select['PUBLIC_PEER'])
      e5.insert(0,select['TITLE'])
      # e6.insert(0,select['OPERATIONAL'])
      # e7.insert(0,select['PEER_MATCH_FOUND'])
      e8.insert(0,select['PK_LINE_ID'])


   
   
   def Add():
      FK_STATION_NAME = e1.get()
      IPSEC = e2.get()
      ACL = e3.get()
      PUBLIC_PEER = e4.get()
      TITLE = e5.get()
      # OPERATIONAL = e6.get()
      # PEER_MATCH_FOUND = e7.get()
      PK_LINE_ID = e8.get()
   
      mssqldb=pyodbc.connect(connectionString)
      mycursor=mssqldb.cursor()
   
      try:
         # sql = "INSERT INTO  [PROJ5].[MAIN_TBL] (FK_STATION_NAME, IPSEC ,ACL ,PUBLIC_PEER , TITLE, OPERATIONAL ,PEER_MATCH_FOUND) VALUES (?, ?, ?, ?)"
         sql = "INSERT INTO  [PROJ5].[MAIN_TBL] (FK_STATION_NAME, IPSEC ,ACL ,PUBLIC_PEER , TITLE) VALUES (?,?,?,?,?)"

         val = (FK_STATION_NAME, IPSEC,ACL,PUBLIC_PEER, TITLE )
         mycursor.execute(sql, val)
         mssqldb.commit()
         #  lastid = mycursor.lastrowid
         messagebox.showinfo("information", "FIREWALL info inserted successfully...")
         e1.delete(0, tk.END)
         e2.delete(0, tk.END)
         e3.delete(0, tk.END)
         e4.delete(0, tk.END)
         e5.delete(0, tk.END)
         # e6.delete(0, tk.END)
         # e7.delete(0, tk.END)
         e8.delete(0, tk.END)

         e2.focus_set()
      except Exception as e:
         messagebox.showinfo("Database Error", e)
         # print(e)
         mssqldb.rollback()
         mssqldb.close()
   
   
 
   
   root = Tk()
   root.geometry("740x450")
   global e1
   global e2
   global e3
   global e4
   global e5
   # global e6
   # global e7
   global e8

   
   tk.Label(root, text="Add New Record : MAIN Table", fg="black", font=(None, 18)).place(x=350, y=10)
   
   tk.Label(root, text="FK_STATION_NAME").place(x=10, y=10)
   tk.Label(root, text="IPSEC").place(x=10, y=40)
   tk.Label(root, text="ACL").place(x=10, y=70)
   tk.Label(root, text="PUBLIC_PEER").place(x=10, y=100)
   tk.Label(root, text="TITLE").place(x=10, y=130)
   # tk.Label(root, text="OPERATIONAL").place(x=310, y=70)
   # tk.Label(root, text="PEER_MATCH_FOUND").place(x=310, y=100)
   tk.Label(root, text="PK_LINE_ID").place(x=310, y=130)
   

   e1 = tk.Entry(root)
   e1.place(x=140, y=10)
   
   e2 = tk.Entry(root)
   e2.place(x=140, y=40)
   
   e3 = tk.Entry(root)
   e3.place(x=140, y=70)
   
   e4 = tk.Entry(root)
   e4.place(x=140, y=100)

   e5 = tk.Entry(root)
   e5.place(x=140, y=130)

   # e6 = tk.Entry(root)
   # e6.place(x=450, y=70)

   # e7 = tk.Entry(root)
   # e7.place(x=450, y=100)

   e8 = tk.Entry(root)
   e8.place(x=450, y=130)
   
   tk.Button(root, text="Add",command = Add,height=2, width= 12).place(x=30, y=190)
   # tk.Button(root, text="update",command = update,height=2, width= 12).place(x=170, y=190)
   # tk.Button(root, text="Delete",command = delete,height=2, width= 13).place(x=310, y=190)
   # tk.Button(root, text="Show",command = show,height=3, width= 13).place(x=360, y=130)

   

   
   root.mainloop()