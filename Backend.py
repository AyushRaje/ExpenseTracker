import numpy
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import xlsxwriter
import Transaction
from datetime import date
import datetime
import pandas as pd
from customtkinter import *



excel_data = pd.read_excel(r"Expense Database\ayushraje.xlsx", header=0)
excel_data.fillna("False", inplace=True)

AllTransactions = []
monthlyExpenseLimit = 20000

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


def loadData():
    for row in excel_data.iterrows():
        temp = Transaction.Transaction()
        if row[1].to_dict()['Debit'] == 'False':
            # its credit
            if row[1].to_dict()['Credit'] != 'False':
                temp.addTransaction('Credit', row[1].to_dict()['Description'], row[1].to_dict()['Comments'],
                                    row[1].to_dict()['Credit'],
                                    "No Acc", row[1].to_dict()['Mode'],
                                    row[1].to_dict()['Transaction Date'])
                AllTransactions.append(temp)
        else:
            # its debit
            if row[1].to_dict()['Debit'] != 'False':
                temp.addTransaction('Debit', row[1].to_dict()['Description'], row[1].to_dict()['Comments'],
                                    row[1].to_dict()['Debit'],
                                    "No Acc", row[1].to_dict()['Mode'],
                                    row[1].to_dict()['Transaction Date'])
                AllTransactions.append(temp)
    return AllTransactions


def printData():
    for i in AllTransactions:
        print("\n------------------")
        i.printTransaction()
        print("------------------\n")


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] // 2, y[i], ha='center')


def drawBarChart():
    totalAmountPerMonth = []
    allMonths = []
    colors = []
    for i in AllTransactions:
        currentMonth = i.date.split(" ")

        if not allMonths or allMonths[len(allMonths) - 1] != currentMonth[1]:
            allMonths.append(currentMonth[1])
            totalAmountPerMonth.append(0)
        if i.type == 'Credit':
            totalAmountPerMonth[len(totalAmountPerMonth) - 1] = totalAmountPerMonth[
                                                                    len(totalAmountPerMonth) - 1] + i.amount;
        else:
            totalAmountPerMonth[len(totalAmountPerMonth) - 1] = totalAmountPerMonth[
                                                                    len(totalAmountPerMonth) - 1] - i.amount;

    for i in totalAmountPerMonth:
        if i >= 0:
            colors.append("#A5C9CA")
        else:
            colors.append("#F86363")

    totalbalance = 0;
    for i in range(len(totalAmountPerMonth)):
        totalbalance = totalbalance + totalAmountPerMonth[i]
    allMonths = allMonths[-12:]
    totalAmountPerMonth = totalAmountPerMonth[-12:]
    colors = colors[-12:]

    plt.style.use('dark_background')
    f = Figure(figsize=(6, 4), dpi=120)
    # f.set_facecolor("black")
    ax = f.add_subplot(111)

    data = totalAmountPerMonth

    ind = numpy.arange(8)  # the x locations for the groups
    width = .5
    rects1 = ax.bar(allMonths, data, width, label=allMonths, color=colors)
    for i in range(len(allMonths)):
        ax.text(i, data[i], f"{round(data[i]):,}", ha='center', weight='bold')
        ax.text

    ax.set_facecolor("black")

    return f;


def currentMonthExpenses():
    i = len(AllTransactions) - 1;
    totalExpense = 0;
    date = AllTransactions[i].date.split(" ");
    thismonth = date[1]
    current = thismonth
    while current == thismonth:
        if (AllTransactions[i].type == "Debit"):
            totalExpense = totalExpense + AllTransactions[i].amount
        if i == 0:
            return round(totalExpense)
        i = i - 1
        date = AllTransactions[i].date.split(" ");
        current = date[1]
    return round(totalExpense)


def getMonthlyExpenseLimit():
    return monthlyExpenseLimit


def currentMonthEarning():
    i = len(AllTransactions) - 1;
    totalEarning = 0;
    date = AllTransactions[i].date.split(" ");
    thismonth = date[1]
    current = thismonth
    while current == thismonth:
        if (AllTransactions[i].type == "Credit"):
            totalEarning = totalEarning + AllTransactions[i].amount
        if i == 0:
            return round(totalEarning)
        i = i - 1
        date = AllTransactions[i].date.split(" ");
        current = date[1]
    return round(totalEarning)


def get_current_month_name():
    i = len(AllTransactions) - 1;
    date = AllTransactions[i].date.split(" ");
    thismonth = date[1]
    return datetime.datetime.strptime(thismonth, '%b').strftime('%B')


def totalLoanToBePaid():
    totalLoan = 0
    for i in AllTransactions:
        tagslist = i.tags[0].split(",")
        if "loan to be payed" in tagslist:
            totalLoan = totalLoan + i.amount
    return round(totalLoan)


def totalLoanToRecieve():
    totalLoan = 0
    for i in AllTransactions:
        deslist = i.description[0].split(",")
        if "loan to recieve" in deslist:
            totalLoan = totalLoan + i.amount
    return round(totalLoan)


def get_names_of_all_months():
    all_months_names = []
    for i in AllTransactions:
        date = i.date.split(" ");
        thismonth = date[1]
        all_months_names.append(thismonth)
    all_months_names = list(dict.fromkeys(all_months_names))
    all_months_names = all_months_names[-12:]
    return all_months_names


def get_percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return percentage / 100
