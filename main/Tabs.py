from tkinter import *
from tkinter import ttk
# Create an instance of Tk
root = Tk()
root.title("Delftstack")

# Create a tab control that manages multiple tabs
tabsystem = ttk.Notebook(root)

# Create new tabs using Frame widget
tab1 = Frame(tabsystem)
tab2 = Frame(tabsystem)

tabsystem.add(tab1, text='First Tab')
tabsystem.add(tab2, text='Second Tab')
tabsystem.pack(expand=1, fill="both")

label = Label(tab1,text="Welcome in Delftstack")

label.grid(column=1,
        row=1,
        padx=40,
        pady=40)
label2nd = Label(tab2, text="Now we are able to see another tab")
label2nd.grid(column=1,
            row=1,
            padx=40,
            pady=40)


Label(tab1, text="Main Table Details", fg="black", font=(None, 19)).place(x=750, y=10)

Label(tab1, text="FK_STATION_NAME").place(x=10, y=10)
Label(tab1, text="IPSEC").place(x=10, y=40)
Label(tab1, text="ACL").place(x=10, y=70)
Label(tab1, text="PUBLIC_PEER").place(x=10, y=100)
Label(tab1, text="TITLE").place(x=10, y=130)
Label(tab1, text="OPERATIONAL").place(x=310, y=70)
Label(tab1, text="PEER_MATCH_FOUND").place(x=310, y=100)
Label(tab1, text="PK_LINE_ID").place(x=310, y=130)


root.mainloop()
