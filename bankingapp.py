import random


# create bankAccount class with attributes of balance and account_number
class BankAccount:

    # initialize classes
    def __init__(self, account_number, balanceacc):
        self.account_number = account_number
        self.balanceacc = balanceacc

    # create depositing method
    def depositing(self):

        while True:
            try:

                amount = float(input("Enter the amount to be deposited: \n"))
                # assign value to amount to be deposited
                if amount <= 0:
                    print("Please enter a Valid amount\n")

                else:
                    self.balanceacc += amount
                    break
            except ValueError:
                print("please Enter a valid number\n")

        print(
            f"You have deposited ${amount} and your total  balance is ${self.balanceacc}\n")

    #  create a withdrawal method to perform withdrawals
    def withdrawing(self):
        while True:
            try:
                amount = float(input("Please enter the amount to be withdrawn: \n"))
                if amount <= 0:
                    print("Withdrawing amount has to be a positive value")
                    break
                if self.balanceacc >= amount:
                    self.balanceacc -= amount
                    print(f"You have withdrawn ${amount} and your total balance is ${self.balanceacc}\n")
                    break
                if amount <= 0:
                    print("Withdrawing amount has to be a positive value")
                else:
                    print("You have insufficient balance to withdraw \n")
            except ValueError:
                print("please Enter a valid number\n")

    # create a withdrawal method to account balances
    def check_balance(self):
        print(f"Your opening balance is $,{self.balanceacc}\n")

    # create a withdrawal method to perform account checks
    def displayBankaccount(self):
        print(f"Your bank account is {self.account_number} and you have opening balance {self.balanceacc}\n")


# create bank classes with methods of depositing,withdraw,transfer,retrieve details
class Bank:

    # initliaze class
    def __init__(self, checkings, balanceacc):
        self.checkings = []
        self.balanceacc = balanceacc

        # self.balance = 0

    # create method to create account, by taking in user input
    def create_account(self):
        print("Thank you for choosing Jewebs Banks.")
        print("I will help you open up a bank account: \n")
        initial_deposit = 300.00
        while True:
            try:
                deposit_amount = int(input("Enter the deposit amount: \n"))

                if deposit_amount >= initial_deposit:
                    while True:
                        account_num = random.randint(100000, 9999999)
                        if account_num not in self.checkings:
                            break
                    new_account = BankAccount(account_num, deposit_amount)
                    self.checkings.append(new_account)
                    print(
                        f"You have deposisted {deposit_amount} and your  checkings account number {account_num} has been created\n")
                    break
                if deposit_amount < initial_deposit:
                    print("The deposit should be more than $300.00\n")
                    continue


            except ValueError:
                print("Please enter a valid amount in figures\n")
                continue
                #return deposit_amount

    # create method to retrieve account details by taking in user input for account

    def get_account(self, ):
        while True:
            try:
                acc_details = int(input("Please enter your account number to retrieve  account details: \n"))

                # use for loop to iterate through accounts to retrieve account information
                for account in self.checkings:
                    if account.account_number == acc_details:
                        return account
                else:
                        print("Account not found\n")
                        break


            except  ValueError:
                print("Please type the correct account number\n")
                break

    # create depositing method
    def deposting(self):  # deposit

    # use get_account method to retrieve account and check any errors
        user_acc = self.get_account()
        if user_acc is None:
            print("Deposit cancelled, Invalid Account, please select continue and select option 1 to create an account.\n")

        else:
         user_acc.depositing()

    # create withdraw method
    def withdraw(self):
        # use get_account method to retrieve account and check any errors and use withdrawing as objects
        user_acc = self.get_account()
        if user_acc is None:
         print("Withdraw cancelled, Invalid Account, please select continue and select option 1 to create an account.\n")
        else:
           user_acc.withdrawing()

    # create transfer method to  take in user input for transfer amount, transfer to and from account.

    def transfer(self):
        while True:
            try:
                Transfer_amount = float(input("Enter the amount to transfer: \n"))
                user_acc = self.get_account()
                if user_acc is None:
                    print("Transfer cancelled. Invalid 'from' account.")
                    return
                acct_from = user_acc
                user_acc2 = self.get_account()
                if user_acc2 is None:
                    print("Transfer cancelled. Invalid 'to' account.")
                    return
                acct_to = user_acc2
                if Transfer_amount > acct_from.balanceacc:
                    print("You do not have sufficient balance to transfer\n")
                    break
                if Transfer_amount <= 0:
                    print("Transfer amount has to be a positive value")
                    break
                else:
                    acct_from.balanceacc -= Transfer_amount
                    acct_to.balanceacc += Transfer_amount
                    print(
                        f"You have transferred ${Transfer_amount} from {acct_from.account_number} to {acct_to.account_number}\n")
                    break
            except ValueError:
                print("Please enter a valid amount")


    # create method account to  account balance

    def account_balance(self):
        user_acc = self.get_account()
        if user_acc is None:
          print("Invalid Account, please select continue and select option 1 to create an account.\n")

        else:
          print(f"Your account balance is ${user_acc.balanceacc}")

    pass


# create display method for menu

def menu():
    print("Welcome to Jewebs Bank.\n")
    print(
        "You can choose 1 : Create Account, 2 : Retrieve account details, 3 : Deposit,  4 : Withdraw , 5 : Transfer , 6 :  End \n")


# create executive_choice for user to select and pass Bank class as a parameter
def executive_choice(Bank):
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        s.create_account()  # create_account method from the instance
    elif choice == "2":
        s.account_balance()  # call the get_account method from the instance
    elif choice == "3":
        s.deposting()  # call the depositing method from the instance
    elif choice == "4":
        s.withdraw()  # call the withdraw method from the instance
    elif choice == "5":
        s.transfer()  # call the transfer method from the instance
    elif choice == "6":
        print("Thank you for using Jewebs Bank...Our Customers Our Pride")
        exit()


# create a recursion function of the executive choice


def continuation_operation():
    while True:

        option = input("Would you like to continue, Please type (y/n) to continue:  ").lower()

        if option == "y":
            executive_choice(Bank)
        elif option == "n":
            print("Thank you for using Jewebs Bank...Our Customers Our Pride")
            exit()
        else:
            print("Invalid choice. Please enter 'y' to continue or 'n' to exit.")
            continue


s = Bank(0, 0)
menu()
continuation_operation()
