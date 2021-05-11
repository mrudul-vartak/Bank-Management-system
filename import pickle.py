import pickle
import os
import pathlib

class Account:
    accno = 0
    name = ''
    deposite = 0
    type = ''

    def createAccount(self):
        self.accno = int(input("Enter the account no :"))
        self.name = input("Enter account holder name: ")
        self.type = input("Enter the type of account [c/s]:")
        self.deposit = int(input("Enter the Initial amount(>=500 for saving and >=1000 for current"))
        print("Account created")


    def showAccount(self):
        print("Account Number : ",self.accno)
        print("Account Holder Name : ",self.name)
        print("Type of Account : ",self.type)
        print("Balance : ",self.deposite)

    def modifyAccount(self):
        print("Acoount Number : ",self.accno)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of account :")
        self.deposite = int(input("Modify Balanc :"))

    def depositAmount(self,amount):
        self.deposit +=amount

    def withdrawAmount(self,amount):
        self.deposit -= amount

    def report(self):
        print(self.accno,"",self.name,"",self.type,"",self.deposit)

    def getAccountNo(self):
        return self.accno

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

def intro():
    print("\t\t\t\t***********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t***********************")

    
    input()

    
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayALL():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accno,"",item.name,"",item.type,"",item.deposit)
        infile.close()
    else:
        print("No records to display")

def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found= False
        for item in mylist:
            if item.accno == num:
                print("Your account Balance is = ",item.deposit)
                found = True
    else:
        print("no records to Search")
    if not found:
       print("No existing record with this number")

def depositAndWitdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('account.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accno == num1:
                if num2 == 1:
                    ammount = int(input("Enter the amount to depost :"))
                    item.deposit += amount
                    print("Your account is updated")
            elif num2 == 2:
                amount = int(input("Enter the amount to withdraw :"))
                if amount <= item.deposit:
                    item.deposit -= amount
                else:
                    print("You canot withdraw larger ammount")
    else:
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')
                
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist= []
        for item in oldlist:
            if item.accno != num:
                newlist.aooend(item)
        os.remove('accounts.data')
        outfile = open('newacccounts.data','wb')
        pickle.dump(newlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accno == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account type :")
                item.deposit = int(input("Enter the Amount :"))
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist,outfile)
        outfile.close()
        os.rename('newaccounts.data','accounts.data')
            
def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.rename('newaccounts.data','accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccount.data','wb')
    pickle.dump(oldlist,outfile)
    outfile.close()
    os.rename('newaccounts.data','accounts.data')

            
#start of the program
ch = ''
x = 0
num = 0
intro()
while x <=100000:
  while ch !=8:
    print('\tMAIN MENU')
    print('\t1.NEW ACCOUNT')
    print('\t2.DEPOSIT AMOUNT')
    print('\t3.WITHDRAW AMOUNT')
    print('\t4.BALANCE ENQUIRY')
    print('\t5.ALL ACCOUNT HOLDER LIST')
    print('\t6.CLOSE AN ACCOUNT')
    print('\t7.MODIFY AN ACCOUNT')
    print('\t8.EXIT')
    print('\tSelect Your Option')
    ch=input()
    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter The account No. :"))
        depositAndwithdraw(num,1)
    elif ch == '3':
        num = int(input("\tEnter The account No. :"))
        depositAndwithdraw(num,2)
    elif ch == '4':
        num = int(input("\tEnter The account No. :"))
        displayAll()
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("\tEnter The account No. :"))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. :"))
        modifyAccount(num)
    elif ch == '8' :
        print("\t Thanks for using bank management system")
        x =100000000
x += x
            
            
