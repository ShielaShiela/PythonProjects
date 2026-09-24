letter = "😊"
print(ord(letter))
print(chr(1234))
word = "helllll         lllllllo"

newword = list(word)
print(newword)
newword[0]="y"
print(str(newword))
print(word)
word = word.replace("l","y")
print(word)
for c in word:
    print(c)

word = word.upper()
newword = word.lower()
print(word)
print(newword)
print(len(word))

a = input()
if a.isdigit():
    print("it is a number")
d = a + 4
print(d)

# if password == "1"234":
#     "1234"-"1234"