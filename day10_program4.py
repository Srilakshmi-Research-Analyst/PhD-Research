#Day10 program4 : Read File line by line

file = open("student.txt", "r")

for line in file:
    print(line)

file.close()