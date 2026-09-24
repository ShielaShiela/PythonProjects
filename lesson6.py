numbers = [4,5,5,7,8]
search = 5

flag = 0
for i in numbers:
    if i == search:
        flag = 1
        break
if flag == 1:
    print("found it!")
else:
    print("its not on the list")


if search in numbers:
    print("found it")
else:
    print("item is not found!")


biggest = 0
for i in numbers:
    if i > biggest:
        biggest = i
print(biggest)

biggest=max(numbers)
print(biggest)

smallest=min(numbers)
print(smallest)
print(numbers)
numbers.append(100)
numbers.insert(3,100)
print(numbers)

numbers2 = (4,5,5,7,8)

# numbers2[0] = 400
# numbers2.append(9)

numbers2D = [[1,2,3], 
             [4,5,6]]

print(numbers2D[0][1])
numbers2D.append([5,6])
numbers2D.append("signature")
for row in numbers2D:
    print(row)