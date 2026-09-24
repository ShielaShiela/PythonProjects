x = 5
y = 0

if y != 0:
    z = x / y
    print(z)
else:
    print("y is zero. cannot do division")


answer = input("Do you want to enter: ")
print(answer.upper())
if answer.upper()  == "YES":
    print("open the door")
else:
    print("keeps closing")