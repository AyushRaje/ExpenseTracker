import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import dexplot as dxp
from Backend import *

selected_month = None
root = None


def get_current_month_transactions():
    i = len(AllTransactions) - 1
    this_month_transactions = []
    while i >= 0:
        currentMonth = AllTransactions[i].date.split(" ")

        if (currentMonth[1] == selected_month):
            this_month_transactions.append(AllTransactions[i])

            i = i - 1
            currentMonth = AllTransactions[i - 1].date.split(" ")
            while currentMonth[1] == selected_month and i > 0:
                this_month_transactions.append(AllTransactions[i])

                i = i - 1
                currentMonth = AllTransactions[i].date.split(" ")
            break
        i = i - 1
    this_month_transactions.reverse()
    return this_month_transactions


def create_expense_bar_chart():
    this_month_transactions = get_current_month_transactions()

    expenses = {}
    for i in this_month_transactions:
        if i.type == "Debit":
            description = i.description[0].split(',')
            for des in description:
                if expenses.get(des) is not None:
                    expenses[des] = expenses[des] + i.amount
                else:
                    expenses[des] = i.amount
    if not expenses:
        return None
    plt.style.use('dark_background')
    f = Figure(figsize=(5, 4), dpi=100)
    # f.set_facecolor("black")
    ax = f.add_subplot(111)

    data = list(expenses.values())

    ind = numpy.arange(8)  # the x locations for the groups
    width = .5
    rects1 = ax.bar(list(expenses.keys()), data, width, label=list(expenses.keys()), color="#A5C9CA")
    for i in range(len(list(expenses.keys()))):
        ax.text(i, data[i], f"{round(data[i]):,}", ha='center', weight='bold')
        ax.text

    ax.set_facecolor("black")

    return f;


def this_month_total_earning():
    this_month_transactions = get_current_month_transactions()
    total_earning = 0
    for i in this_month_transactions:
        if i.type == 'Credit':
            total_earning = total_earning + i.amount;
    return round(total_earning)


def this_month_total_expenses():
    this_month_transactions = get_current_month_transactions()
    total_expense = 0
    for i in this_month_transactions:
        if i.type == 'Debit':
            total_expense = total_expense + i.amount;

    return round(total_expense)



def create_current_month_expenses_frame():
    current_month_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    # adding bar chart
    if create_expense_bar_chart() != None:
        canvas = FigureCanvasTkAgg(create_expense_bar_chart(), master=current_month_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, columnspan=1, padx=20, sticky="nw")


    
    font_cashflowLabel = customtkinter.CTkFont(family="Poppins Regular", size=15)
    label_cashflowLabe = customtkinter.CTkLabel(master=current_month_frame,
                                                text="Cash flow for " + datetime.datetime.strptime(selected_month,
                                                                                                   '%b').strftime('%B'),
                                                anchor="w",
                                                font=font_cashflowLabel)
    label_cashflowLabe.grid(row=4, column=0, sticky="nw")

    # Earned label
    font_earnedLabel = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_earnedLabel = customtkinter.CTkLabel(master=current_month_frame, text="EARNED", anchor="w",
                                               font=font_earnedLabel)
    label_earnedLabel.grid(row=4, column=0, pady=20, sticky="nw")

    # Earned amount label
    font_amountEarned = customtkinter.CTkFont(family="Poppins Bold", size=10)
    label_amountEarned = customtkinter.CTkLabel(master=current_month_frame,
                                                text="Rs." + str(f"{this_month_total_earning():,}"),
                                                anchor="w",
                                                font=font_amountEarned)
    label_amountEarned.grid(row=4, column=0, padx=150, pady=20, sticky="nw")

    # progess bar
    progressbar = customtkinter.CTkProgressBar(master=current_month_frame)
    progressbar.set(get_percentage(this_month_total_earning(), getMonthlyExpenseLimit()))
    progressbar.grid(row=4, column=0, pady=40, sticky="nw")

    # SPENT label
    font_spentLabel = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_spentLabel = customtkinter.CTkLabel(master=current_month_frame, text="SPENT", anchor="w",
                                              font=font_spentLabel)
    label_spentLabel.grid(row=4, column=0, pady=60, sticky="nw")

    # SPENT amount label
    font_spentAmount = customtkinter.CTkFont(family="Poppins Bold", size=10)
    label_spentAmount = customtkinter.CTkLabel(master=current_month_frame,
                                               text="Rs." + str(f"{this_month_total_expenses():,}"),
                                               anchor="w",
                                               font=font_spentAmount)
    label_spentAmount.grid(row=4, column=0, padx=150, pady=60, sticky="nw")

    # progess bar
    progressbar = customtkinter.CTkProgressBar(master=current_month_frame)
    progressbar.set(get_percentage(this_month_total_expenses(), getMonthlyExpenseLimit()))
    progressbar.grid(row=4, column=0, pady=80, sticky="nw")

    # Remaining cashflow amount label
    font_remainingAmount = customtkinter.CTkFont(family="Poppins Bold", size=20)
    if (this_month_total_earning() - this_month_total_expenses() < 0):
        color = "red"
    else:
        color = "green"
    label_remainingAmount = customtkinter.CTkLabel(master=current_month_frame, text_color=color,
                                                   text="Rs." + str(
                                                       f"{this_month_total_earning() - this_month_total_expenses():,}"),
                                                   anchor="w", font=font_remainingAmount)
    label_remainingAmount.grid(row=4, column=0, padx=210, pady=45, sticky="nw")

    # Remaning label
    font_remainingLabel = customtkinter.CTkFont(family="Poppins Regular", size=10)
    label_remaining = customtkinter.CTkLabel(master=current_month_frame, text="REMAINING", anchor="w",
                                             font=font_remainingLabel)
    label_remaining.grid(row=4, column=0, pady=70, padx=210, sticky="nw")

    current_month_frame.grid(row=1, column=0, pady=20, padx=20, sticky="nsew")


def select_month_event(month):
    global selected_month
    selected_month = month
    create_current_month_expenses_frame()


def create_expenses_frame(Root):
    global root
    expenses_frame = customtkinter.CTkFrame(Root, corner_radius=0, fg_color="transparent")
    root = expenses_frame
    month_select_menu = customtkinter.CTkOptionMenu(master=expenses_frame, values=get_names_of_all_months(),
                                                    command=select_month_event)
    month_select_menu.grid(row=0, column=0, padx=20, sticky="nw")
    return expenses_frame
