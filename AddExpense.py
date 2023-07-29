from customtkinter import *
from datetime import date
import sqlite3
import Login

root=CTkToplevel()
test=Login.login_label
CTkLabel(root,text=test).pack()
root.mainloop()