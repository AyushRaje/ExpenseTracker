totalBalance = 0


class Transaction:
    type = None  
    amount = None  
    description = []
    comments = None  
    date = None  
    acc = None  
    # bank = None  # bank
    mode = None  
    availableBalance = None  

    def addTransaction(myself, type, description, comments, amount, acc, mode, date=None):
        global totalBalance
        myself.type = type
        myself.mode = mode
        myself.amount = amount
        myself.comments = comments
        myself.acc = acc
        # myself.bank = bank
        myself.description = description.split(",")
        if date is not None:
            myself.date = date
        else:
            myself.date = date.today().strftime("%d/%m/%Y")
        if type == "Debit":
            myself.availableBalance = totalBalance - amount
            totalBalance = myself.availableBalance

        else:
            myself.availableBalance = totalBalance + (amount)
            totalBalance = myself.availableBalance

    def printTransaction(self):
        print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("Type: " + self.type)
        print("description: " + str(self.description))
        print("amount: " + str(self.amount))
        # print("availableBalance: " + str(self.availableBalance))
        print("comments: " + self.comments)
        print("mode: " + self.mode)
        print("date: " + self.date)
        print("acc: " + self.acc)
        # print("bank: " + self.bank)
        print(">>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n")
