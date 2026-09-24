
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.name = None
        self.accountNo = None
        self.address = None

    def deposit(self):
        amount = int(input("Enter Amount to Deposit: "))
        self.balance += amount

    def withdraw(self):
        amount = int(input("Enter Amount to Withdraw: "))
        self.balance -= amount

    def showBalance(self):
        print(f"Your current balance {self.balance}")

    def updateAddress(self):
        pass


person1 = BankAccount()
print("Create Account")
accountno = input("Enter account no: ")
accountname = input("Enter Name: ")
initialamount = int(input("Enter Initial Money: "))

person1.accountNo = accountno
person1.name = accountname
person1.balance = initialamount

while True:

    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show Balance")
    select = input("Enter Menu: ")

    if select == "1":
        person1.deposit()
    elif select == "2":
        person1.withdraw()
    elif select == "3":
        person1.showBalance()