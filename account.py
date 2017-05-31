class account:
    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def __str__(self):
        return "account number" + str(self.accountno)+"\n"+ \
                "balance:"+ str(self.balance)

class currentaccount(account):
    def __init__(self,accountno):
        account.__init__(self,accountno)

    def __str__(self):
        retstr = "account type: Current\n"
        retstr += account.__str__(self)
        return retstr

    def withdraw(self,amount):
        if (amount > self.balance or self.balance <15000):
            print("Insufficient Balance")
        else:
            self.balance = (self.balance - amount) - amount*0.1
        return self.balance

class savingsaccount(account):
    def __init__(self, accountno):
        account.__init__(self, accountno)

    def __str__(self):
        retStr = "account type: savings\n"
        retStr += account.__str__(self)
        return retStr

    def withdraw(self,amount):
        if (amount > self.balance or self.balance < 1000):
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
        return self.balance


nihal= account(1234567,20000)

account.deposit(nihal,3000)
print(account.__str__(nihal))
savingsaccount.withdraw(nihal,200)
print(savingsaccount.__str__(nihal))
currentaccount.withdraw(nihal,1000)
print(currentaccount.__str__(nihal))