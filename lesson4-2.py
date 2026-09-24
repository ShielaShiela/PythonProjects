#definition
def multiply(num1, num2, num3=1):

    ans = num1 * num2 * num3

    return ans

def addContact(name, phoneNo=12234):
    print("Name: ",name)
    print("Phone No:", phoneNo)

    print("Added Successfully!!!")

def getTwoNumbers():

    a = int(input("Enter 1: "))
    b = int(input("Enter 2: "))

    return a, b 

def menu():
    print("1. coke")
    print("2. water")
    print("3. milk")

def mainmenu():

    print("1. Show Drinks")
    print("2. Pay Bill")
    print("3. Exit Program")

def drinkprogram():
    mainmenu()
    select = input("Choice (1-3):")

    if select == "1":
        menu()

while True:
    drinkprogram()
    print()
    



# print(getTwoNumbers())
# n1, n2 = getTwoNumbers()
# print(n1, n2)
# a = multiply(n1,n2)
# print(a)

# addContact("shiela")
# addContact("shiela",123456)