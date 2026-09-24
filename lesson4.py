def showContactDetails():
    print("Name: Shiela")
    print("Phone No: 12345678")

def sayHello():
    print("Hello")

def welcomeUser(username):
    print("Welcome",username)

def problem1():
    count = 0 

    while True:

        word = input()

        if word == "stop":
            break
        else:
            count += 1

    print("Word count: ", count)

def problemBMI():
    n = 5 
    for i in range(1,n):
        print("Person",i)
        a = int(input("Enter weight: "))
        b = float(input("Enter Height: "))

        print("BMI: ", a / b ** 2)


#call
showContactDetails()
showContactDetails()
sayHello()
welcomeUser("shielasan")
welcomeUser("Leo")
problem1()