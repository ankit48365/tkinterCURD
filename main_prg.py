
import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
from tkinter import *
from main import tkcurdpg as tkpg

# tkpg.outer()


def STATION_MODIFY():
    # from main import tkcurdpg as tkpg
    tkpg.outer()

def AGENCY_MODIFY():
    print("Agency")

def MAIN_MODIFY():
    print("MAIN")


root = Tk()
root.geometry("400x160")

tk.Label(root, text="!! Welcome !!", fg="black", font=(None, 18)).place(x=130, y=20)
# tk.Label(root, text="STATION_NAME").place(x=10, y=10)
Button(root, text="Station Table",command = STATION_MODIFY,height=2, width= 10).place(x=40, y=70)
Button(root, text="Agency Table",command = AGENCY_MODIFY,height=2, width= 10).place(x=155, y=70)
Button(root, text="Main Table",command = MAIN_MODIFY,height=2, width= 9).place(x=270, y=70)



root.mainloop()
