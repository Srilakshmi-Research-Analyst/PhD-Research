#Day6 program2 : Print Multiplication Table 

num = int(input("Enter a number:"))

for i in range(1, 11):
    print(num, "*" , i, "=", num * i)