
# myfile = open("file1.txt","a")

# myfile.write("Taiwan\n")
# myfile.write("Taiwan\n")
# myfile.write("Japan\n")
# myfile.close()

with open("file3.txt","r") as inFile:
    if inFile is None:
        print("File not found")
    else:
        pass

inFile = open("file3.txt","r")
total = 0
inputs = inFile.readlines()
print(inputs)
for line in inputs:
    line = line.strip()
    print(line)
    #str to int
    total += int(line)

print(total)