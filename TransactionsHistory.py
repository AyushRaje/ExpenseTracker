import tkinter
from tkinter import LEFT, BOTH, VERTICAL, Y, RIGHT, ttk

from Expenses import *

root = None
transaction_history_month = None


def show_all_transactions():
    all_transactions_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    # Create A Canvas
    if customtkinter.get_appearance_mode() == 'Light':
        bg = '#f0ecec'
    else:
        bg = root["bg"]
    my_canvas = tkinter.Canvas(all_transactions_frame, bg=bg, bd=0, highlightthickness=0, width=900, height=500)
    my_canvas.grid(row=1, column=0)

    # Add A Scrollbar To The Canvas
    my_scrollbar = customtkinter.CTkScrollbar(all_transactions_frame, orientation="vertical", command=my_canvas.yview)
    my_scrollbar.grid(row=1, column=0, sticky="ens")

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    list_of_transactions_frame = customtkinter.CTkFrame(my_canvas, corner_radius=0, fg_color="transparent")
    list_of_transactions_frame.grid(row=0, column=0, columnspan=3)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=list_of_transactions_frame, anchor="nw")

    i = 0
    this_month_transactions = get_current_month_transactions_history()
    # transaction attributes row

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Date",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=0, columnspan=6, padx=20, pady=20, sticky='nw')

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Description",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=1, padx=20, pady=20, sticky='nw')

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Type",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=2, padx=20, pady=20, sticky='nw')

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Amount",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=3, padx=20, pady=20, sticky='nw')

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Comments",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=4, padx=20, pady=20, sticky='nw')

    temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                        text="Mode",
                                        compound="left", wraplength=100, justify="left", text_color="#395B64",
                                        font=customtkinter.CTkFont(size=15, weight="bold"))
    temp_label.grid(row=i, column=5, padx=20, pady=20, sticky='nw')

    # temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
    #                                     text="Bank",
    #                                     compound="left", wraplength=100, justify="left", text_color="#395B64",
    #                                     font=customtkinter.CTkFont(size=15, weight="bold"))
    # temp_label.grid(row=i, column=6, padx=20, pady=20, sticky='nw')
    i = 1
    #print transaction details in table
    for transaction in this_month_transactions:
        # transaction details
        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=transaction.date,
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=0, padx=20, pady=20, sticky='nw')

        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=transaction.description,
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=1, padx=20, pady=20, sticky='nw')

        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=transaction.type,
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=2, padx=20, pady=20, sticky='nw')

        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=f"{transaction.amount:,}",
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=3, padx=20, pady=20, sticky='nw')

        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=transaction.comments,
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=4, padx=20, pady=20, sticky='nw')

        temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
                                            text=transaction.mode,
                                            compound="left", wraplength=100, justify="left",
                                            font=customtkinter.CTkFont(size=15, weight="bold"))
        temp_label.grid(row=i, column=5, padx=20, pady=20, sticky='nw')

        # temp_label = customtkinter.CTkLabel(master=list_of_transactions_frame,
        #                                     text=transaction.bank,
        #                                     compound="left", wraplength=100, justify="left",
        #                                     font=customtkinter.CTkFont(size=15, weight="bold"))
        # temp_label.grid(row=i, column=6, padx=20, pady=20, sticky='nw')
        i = i + 1
    all_transactions_frame.grid(row=1, column=0)


def set_month_event(month):
    global transaction_history_month
    transaction_history_month = month
    show_all_transactions()


def get_current_month_transactions_history():
    i = len(AllTransactions) - 1
    this_month_transactions = []
    while i >= 0:
        currentMonth = AllTransactions[i].date.split(" ")

        if (currentMonth[1] == transaction_history_month):
            this_month_transactions.append(AllTransactions[i])

            i = i - 1
            currentMonth = AllTransactions[i - 1].date.split(" ")
            while currentMonth[1] == transaction_history_month and i > 0:
                this_month_transactions.append(AllTransactions[i])

                i = i - 1
                currentMonth = AllTransactions[i].date.split(" ")
            break
        i = i - 1
    this_month_transactions.reverse()
    return this_month_transactions


def create_transactions_history_frame(Root):
    global root
    transactions_history_frame = customtkinter.CTkFrame(Root, corner_radius=0, fg_color="transparent")
    root = transactions_history_frame
    month_select_menu = customtkinter.CTkOptionMenu(master=transactions_history_frame, values=get_names_of_all_months(),
                                                    command=set_month_event)
    month_select_menu.grid(row=0, column=0, padx=20, sticky="nw")
    return transactions_history_frame
