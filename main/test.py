# import pyodbc
# server = 'ak-az-sqlserver.database.windows.net'
# database = 'ak-az-sqlserver'
# username = 'admin4'
# password = '{P@ssword2021}'   
# driver= '{ODBC Driver 17 for SQL Server}'
# connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'


# mssqldb = pyodbc.connect(connectionString)
# mycursor = mssqldb.cursor()
# mycursor.execute("SELECT TOP 3 * from PROJ5.SITE_TBL")
# records = mycursor.fetchall()
# print(records)


# Import module
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()