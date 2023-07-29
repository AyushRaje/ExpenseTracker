import customtkinter
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from Backend import *
import sqlite3
import subprocess
from tkcalendar import Calendar
import tkinter as tk
# import Login
import openpyxl

def createDashboardFrame(root):
    
    loadData()
    home_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    
    def Clear():
        entry_amount.delete(0,END)
        entry_date.delete(0,END)
        entry_description.delete(0,END)
        optionmenu_cat.set("Food")
        optionmenu_pay.set("Paytm")
        optionmenu_trans.set("Credit")
    
    def Submit():
        Add_details={}
        if optionmenu_trans.get()=="Credit":
            Add_details = {'Transaction Date':[entry_date.get()],'Description':[optionmenu_cat.get()],'Debit':[int(0)],'Credit':[int(entry_amount.get())],'Comments':[entry_description.get()],'Bank':[optionmenu_pay.get()]}
    
        else:
            Add_details = {'Transaction Date':[entry_date.get()],'Description':[optionmenu_cat.get()],'Debit':[int(entry_amount.get())],'Credit':[int(0)],'Comments':[entry_description.get()],'Bank':[str(optionmenu_pay.get())]}
        
        
        df=pd.DataFrame(Add_details)
        print(df)
        writer=pd.ExcelWriter(r'Expense Database\ayushraje.xlsx',engine='openpyxl',mode='a',if_sheet_exists="overlay")
        reader=pd.read_excel(r"Expense Database\ayushraje.xlsx")
        df.to_excel(writer,sheet_name="Sheet1", index=False, header=False, startrow=len(reader) + 1)
        writer.close()
        entry_amount.delete(0,END)
        entry_date.delete(0,END)
        entry_description.delete(0,END)
       
           
    canvas = FigureCanvasTkAgg(drawBarChart(), master=home_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=2,columnspan=5,sticky="ns",padx=120)

    
    
    font_expenseLimit = customtkinter.CTkFont(family="Poppins Regular", size=25)
    Add_expense=customtkinter.CTkLabel(master=home_frame,text="Add Your Expense",font=font_expenseLimit)
    Add_expense.grid(row=1,column=2,sticky="ns",columnspan=5,pady=10)   
   

    
    labels_fonts = customtkinter.CTkFont(family="Poppins Bold", size=18)
    label_date = customtkinter.CTkLabel(master=home_frame, text="Date",font=labels_fonts)
    label_date.grid(row=3, column=2,pady=20, sticky="ns")


    entry_date=customtkinter.CTkEntry(master=home_frame,font=labels_fonts)
    entry_date.grid(row=4,column=2,sticky="ns")
    date=str(entry_date.get())
    label_amount = customtkinter.CTkLabel(master=home_frame, text="Amount",font=labels_fonts)
    label_amount.grid(row=3, column=3,pady=20,padx=(55,0),sticky="ns")
    
    entry_amount=customtkinter.CTkEntry(master=home_frame,font=labels_fonts)
    entry_amount.grid(row=4,column=3,padx=(55,0),sticky="ns")
    
    label_type = customtkinter.CTkLabel(master=home_frame, text="Category",font=labels_fonts)
    label_type.grid(row=3, column=4,pady=20, sticky="ns")
    
    
    def optionmenu_category(choice):
        print("optionmenu dropdown clicked:", choice)
      
        
    
    optionmenu_cat = customtkinter.CTkOptionMenu(master=home_frame, values=["Food", "Groceries","Bills","Online Purchase","Others"],
                                         command=optionmenu_category)
    optionmenu_cat.grid(row=4,column=4,sticky="ns")
    
    label_transaction= customtkinter.CTkLabel(master=home_frame, text="Transaction",
                                                       font=labels_fonts)
    label_transaction.grid(row=3, column=5, pady=20, sticky="ns")
    
    
    def optionmenu_transaction(choice):
        print("optionmenu dropdown clicked:", choice)

    
    
    optionmenu_trans = customtkinter.CTkOptionMenu(master=home_frame, values=["Credit", "Debit"],
                                         command=optionmenu_transaction)
    optionmenu_trans.grid(row=4,column=5,sticky="ns")
    

    label_payment= customtkinter.CTkLabel(master=home_frame, text="Mode of Payment",
                                                       font=labels_fonts)
    label_payment.grid(row=5, column=2, pady=20,padx=20, sticky="ns")
        
    
    def optionmenu_payment(choice):
        print("optionmenu dropdown clicked:", choice)
        sel_pay=choice
        

    
    
    optionmenu_pay = customtkinter.CTkOptionMenu(master=home_frame, values=["Paytm", "Gpay","Phonepay","AmazonPay","Cash","Others"],
                                         command=optionmenu_payment)
    optionmenu_pay.grid(row=6,column=2,sticky="ns")
    
    
    
    label_description= customtkinter.CTkLabel(master=home_frame, text="Description",
                                                       font=labels_fonts)
    label_description.grid(row=5, column=4, pady=20, sticky="ns")
    
    entry_description=customtkinter.CTkEntry(master=home_frame,font=labels_fonts,width=300)
    entry_description.grid(row=6,column=4,sticky="ns")
    
    
    
        
     
    
    add_button=customtkinter.CTkButton(master=home_frame, text="Add Expense",fg_color="green",width=180,height=40,command=Submit)
    add_button.grid(row=7,column=3,sticky="ns",pady=35,padx=20)
    
    clear_button=customtkinter.CTkButton(master=home_frame, text="Clear All",fg_color="red",width=180,height=40,command=Clear)
    clear_button.grid(row=7,column=4,sticky="ns",pady=35)
    
    
   
    
    
    return home_frame
