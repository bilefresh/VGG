"""
Created by Bilesanmi Faruk
"""
accounts = {
    "farouk@vgg.com": {"password": "password", "balance": 3000000.00}
    }

def CreateAccount():
    email = input("Please enter your email address: ").lower()
    if ("@" and ".") in email:
        if email in accounts.keys():
            print("Sorry but this email is attached to an account that already exists")
        else:
            password = input("Please enter your password: ")
            accounts[email] = {"password": password, "balance": 0.0}
            print(accounts[email])
            print("Your account has been created successfully")
            log = input("Would you like to login into your account now? (Enter yes or no):  ").lower()
            if log == "yes":
                Transaction()
            else:
                print("Goodbye, Thank you for choosing VGG")
    else:
        print("This is not a valid email, please try again")
        CreateAccount()
def Transaction():
    email = input("Enter your eamil address: ").lower()
    if email not in accounts.keys():
        print("Sorry Account doesn't exist")
        answer = input("Would you like to create an account (Enter yes or no): ")
        if answer == "yes":
            CreateAccount()
        else:
            print("Thank you for choosing us")
    else:
        while True: 
            password = input("Enter your password: ")
            if password == accounts[email]["password"]:
                print("Welcome, "+email)
                count = 0
                while True:
                    if count >= 1:
                        transaction = input("\nWhat else would you like to do\nType 1: Check balance\n2: Deposit\n3: Withdraw\n4: Transfer\nl: to logout\nq: to quit\n")
                    else:
                        transaction = input("What would you like to do\nType 1: Check balance\n2: Deposit\n3: Withdraw\n4: Transfer\nl: to logout\nq: to quit\n")
                        count+=1
                    if transaction == "1":
                        balance(email)
                    elif transaction == "2":
                        deposit(email)
                    elif transaction == "3":
                        withdraw(email)
                    elif transaction == "4":
                        transfer(email)
                    elif transaction == "l":
                        print("Logging you out ...\n")
                        begin()
                    elif transaction =="q":
                        print("Goodbye, Thank you for banking with us")
                        break
                    else:
                        print("Invalid Transaction, select one of the above")
                    
                break
            else:
                print("Incorrect Password")

def balance(email):
    balance = accounts[email]["balance"]
    print("Your balance is ", balance)
    print("Thank you for banking with us")

def deposit(email):
    cash = input("Enter the amount you want to deposit: ")
    while True:
        try:
            cash = float(cash)
            if cash > 0.0:
                break
            else:
                print("Invalid amount, enter figures above 0 only")
                cash = input("Enter the amount you want to deposit: ")
        except ValueError:
            print("Invalid amount, enter figures only")
            cash = input("Enter the amount you want to deposit: ")
    balance = accounts[email]["balance"]
    accounts[email]["balance"] = balance + cash
    new_balance = accounts[email]["balance"]
    print("You have deposited ", cash, "\nYour new balance is ", new_balance)
    print("Thank you for banking with us")

def withdraw(email):
    withdraw = input("Enter the amount youo want to withdraw: ")
    while True:
        try:
            withdraw = float(withdraw)
            if withdraw > 0.0:
                break
            else:
                print("Invalid amount, enter figures above 0 only")
                withdraw = input("Enter the amount you want to deposit: ")
        except ValueError:
            print("Invalid amount, enter figures only")
            withdraw = input("Enter the amount you want to deposit: ")
    balance = accounts[email]["balance"]
    if balance < withdraw:
        print("Insufficient funds, your current balance is", balance)
        deposit = input("Would you make a Deposit? Enter (yes or no)").lower()
        if deposit == "yes":
            deposit(email)
        elif deposit== "no":
            print("Thank you for banking with us")
        else:
            print("Invalid selection")
    else:
        accounts[email]["balance"] = balance - withdraw
        new_balance = accounts[email]["balance"]
        print("You have withdrawn", withdraw, "Your new balance is ", new_balance)
        print("Thank you for banking with us")

def transfer(email):
    recipient = input("Please enter the beneficiary's email: ").lower()
    if recipient not in accounts.keys():
        print("Beneficiary does not exist, Please try again")
        transfer(email)
    cash_transfer = input("Please enter the amount to transfer: ")
    while True:
        try:
            cash_transfer = float(cash_transfer)
            if cash_transfer > 0.0:
                break
            else:
                print("Invalid amount, please enter figures above 0 only")
                cash_transfer = input("Please enter the amount to transfer: ")
        except ValueError:
            print("Invalid amount, please enter figures only")
            cash_transfer = input("Please enter the amount to transfer: ")

    balance = accounts[email]["balance"]
    if balance < cash_transfer:
        print("Insufficient funds, your current balance is", balance)
        deposit = input("Would you make a Deposit? (Enter yes or no)").lower()
        if deposit == "yes":
            deposit(email)
        elif deposit == "no":
            print("Thank you for banking with us")
        else:
            print("Invalid selection")
            
    else:
        accounts[email]["balance"] = balance - cash_transfer
        new_balance = accounts[email]["balance"]
        recipient_balance = accounts[recipient]["balance"]
        accounts[recipient]["balance"] = recipient_balance + cash_transfer
        print("You have transferred", cash_transfer, "to", recipient, "Your new balance is ", new_balance)

def begin():
    greet = input("Hello, welcome to the VGG bank\nWhat would you like to do\n1. Create Account\n2. Perform a Transaction\nq to quit\n")

    while True:
        if greet == "1" or "2" or "q":
            break
        else:
            print("Invalid selection")
    if greet == "1":
        CreateAccount()
    elif greet == "2":
        Transaction()
    elif greet == "q":
        print("Goodbye!\nThank you for banking with us.")
    else:
        print("Invalid selection")

begin()
