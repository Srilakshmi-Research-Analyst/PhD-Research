#Day7 Program5 : Factorial using a function

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
num = int(input("Enter a number:"))
print("Factorial=", factorial(num))