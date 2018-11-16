
class account:
    no_of_accs=0

    def open_account(self):
        name  = raw_input('Account Holder Name:\t')
        acc_bal = input('Enter Deposit amount:\t')
        acc_type = input('Account Type (Saving/Current):\t')
        address = raw_input('Account Holder Address:\t')
        
        account.no_of_accs = account.no_of_accs + 1
        self.acc_no = account.no_of_accs +1
        self.acc_bal = acc_bal
        self.acc_type = acc_type
        self.name = name
        self.address = address

    def display(self):
        print 'Ac Holder Name # %s , Ac #: %d, Current Bal =%f \nAddress %s'%(self.name,self.acc_no, self.acc_bal, self.address)
        
    def withdraw(self):
        amount = input('Enter amount to dispense:\t')
        if self.acc_bal > 0 and self.acc_bal < amount:
            self.acc_bal -= amount
        else:
            print 'Insuffient fund'
            
    def deposit(self):
        amount = input('Enter amount to deposit:\t')
        self.acc_bal += amount
        print 'Amount deposited %d'%(amount)


accounts = dict()
acc1 = account()
acc2 = account()
acc1.open_account()
#acc2.open_account()
accounts = {1,acc1}
accounts = {2,acc2}

print accounts

print acc1.display()
