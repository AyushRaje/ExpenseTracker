from customtkinter import *
from tkinter import *
import sqlite3 
import os
from PIL import Image
import subprocess
from CTkMessagebox import CTkMessagebox
import xlsxwriter
import customtkinter
from Dashboard import *
from TransactionsHistory import *
from Expenses import *
from Backend import *



class App(customtkinter.CTkToplevel):
    def __init__(self):
        loadData()
        super().__init__()
        self.title("E-Wallet")
        self.geometry("1080x750")

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "house.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "house.png")),
                                                 size=(20, 20))
        self.dollar_sign = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "dollar.png")),
            dark_image=Image.open(os.path.join(image_path, "dollar.png")), size=(20, 20))
        self.expenses = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "statistics.png")),
            dark_image=Image.open(os.path.join(image_path, "statistics.png")), size=(20, 20))
        self.all_accounts = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "all_accounts.png")),
            dark_image=Image.open(os.path.join(image_path, "all_accounts.png")), size=(20, 20))
        self.all_transactions = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "wallet.png")),
            dark_image=Image.open(os.path.join(image_path, "wallet.png")), size=(20, 20))

        # navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" Options",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Expenses",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.expenses, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="All Transactions",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.all_transactions, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        
        font_balance = customtkinter.CTkFont(family="Poppins Regular", size=15)
        label_balance = customtkinter.CTkLabel(master=self.navigation_frame, text="Balance", anchor="w", font=font_balance)
        label_balance.grid(row=5, column=0,sticky="ns")
        
        if round(AllTransactions[len(AllTransactions) - 1].availableBalance) < 0:
            color = "red"
        else:
            color = "green"
    
        font_totalBalance = customtkinter.CTkFont(family="Poppins Bold", size=20)
        label_totalBalance = customtkinter.CTkLabel(master=self.navigation_frame, text="Rs." + str(f"{round(AllTransactions[len(AllTransactions) - 1].availableBalance):,}"
        ), text_color=color,font=font_totalBalance)
        label_totalBalance.grid(row=6, column=0,sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        #  home frame
        self.home_frame = createDashboardFrame(self)
        # create second frame
        self.second_frame = create_expenses_frame(self)

        # create third frame
        self.third_frame = create_transactions_history_frame(self)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, columnspan=5, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)





root=CTk()
root.title("E-Wallet")
root.geometry("400x400")
conn=sqlite3.connect(r"LoginInfo.db")
cur=conn.cursor()
# global test
# test="Tested"
# cur.execute("CREATE TABLE Users( first_name text,last_name text,user_name text,password text,cnf_password text)")

def UserRegister():
    conn=sqlite3.connect(r"LoginInfo.db")


    cur= conn.cursor()
    if password==cnf_pass:
        cur.execute("INSERT INTO Users VALUES(:fname,:lname,:uname,:pass,:cnfpass)",
                {
                    'fname':fname.get(),
                    'lname':lname.get(),
                    'uname':uname.get(),
                    'pass':password.get(),
                    'cnfpass':cnf_pass.get()    
                }
                
                
                )
    
        conn.commit()
        conn.close()
        path=str(uname.get())+".xlsx"
        signup_win.destroy()
        workbook=xlsxwriter.Workbook('Expense Database\ '+path)
        worksheet=workbook.add_worksheet()
        workbook.close()
    
    else:
        CTkMessagebox(title="Error",message="Please Enter Same Password")    
        
    
def Clear():
    fname.delete(0,END)
    lname.delete(0,END)
    uname.delete(0,END)
    password.delete(0,END)
    cnf_pass.delete(0,END)    

def NewUser():
    path=""
    global fname
    global lname
    global uname
    global password
    global cnf_pass
    global signup_win
    signup_win=CTkToplevel()
    signup_win.title("Signup")
    # signup_win.geometry("700x700")
    
    fname=CTkEntry(signup_win,width=300)
    fname.grid(row=0,column=1,padx=20,pady=10)

    lname=CTkEntry(signup_win,width=300)
    lname.grid(row=1,column=1,padx=20,pady=10)

    uname=CTkEntry(signup_win,width=300)
    uname.grid(row=2,column=1,padx=20,pady=10)

    password=CTkEntry(signup_win,show="*",width=300)
    password.grid(row=3,column=1,padx=20,pady=10)

    cnf_pass=CTkEntry(signup_win,width=300)
    cnf_pass.grid(row=4,column=1,padx=20,pady=10)
    
    CTkLabel(signup_win,text="Firstname").grid(row=0,column=0,padx=10)
    CTkLabel(signup_win,text="Lastname").grid(row=1,column=0,padx=10)
    CTkLabel(signup_win,text="Username").grid(row=2,column=0,padx=10)
    CTkLabel(signup_win,text="Set Password").grid(row=3,column=0,padx=10)
    CTkLabel(signup_win,text="Confirm Password").grid(row=4,column=0,padx=10)
    
    user_submit=CTkButton(signup_win,text="Register",fg_color="green",command=UserRegister).grid(row=5,column=0,pady=15,padx=(150,0))
    user_clear=CTkButton(signup_win,text="Clear",fg_color="Red",command=Clear).grid(row=5,column=1,pady=15)
   

def LoginUser():
    global Info
    conn=sqlite3.connect(r"LoginInfo.db")
    cur=conn.cursor()
    global selected_user
    selected_user=str(login_entry.get())
    selected_pass=str(pass_entry.get())
    cur.execute("SELECT * FROM Users WHERE user_name = ? AND password=? ",(selected_user,selected_pass))
    Info=cur.fetchone()
    if(Info):
        # Exp_conn=sqlite3.connect(r"Expense Database\Expenses.db")
        # Exp_cur=Exp_conn.cursor()
        
        # Exp_cur.execute("CREATE TABLE IF NOT EXISTS "+selected_user+"(Transaction_date text, Description text, Credit INT, Debit INT, Payment text, Comment text)")
        # Exp_conn.commit()
        # Exp_conn.close()
        login_entry.delete(0,END)
        pass_entry.delete(0,END)
        app=App()
        app.mainloop()
        
        
    else:
        CTkMessagebox(title="Error",message="Invalid Password or Username")    
    # conn.commit()
        

CTkLabel(root,text="User Login",font=("Arial",20)).grid(row=2,column=1,pady=20,padx=130)

global login_entry
global pass_entry
login_label=CTkLabel(root,text="Username",font=("Arial",15)).grid(row=4,column=1,pady=(20,0),padx=100)
login_entry=CTkEntry(root,width=200)
login_entry.grid(row=6,column=1,padx=100)

pass_label=CTkLabel(root,text="Password",font=("Arial",15)).grid(row=7,column=1,pady=(20,0),padx=100)
pass_entry=CTkEntry(root,show="*",width=200)
pass_entry.grid(row=8,column=1,padx=100)

login_btn=CTkButton(root,text="Login",font=("Arial",15),fg_color="green",command=LoginUser).grid(row=9,column=1,pady=(20,0),padx=100)
signup_btn=CTkButton(root,text="Signup",font=("Arial",15),fg_color="blue",command=NewUser).grid(row=10,column=1,pady=(20,0))


conn.commit()
conn.close()

root.mainloop()
