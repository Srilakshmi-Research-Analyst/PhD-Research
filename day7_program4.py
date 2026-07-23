#Day7 Program4 : Even or Odd using Function

def check_even_odd(num):
    if num % 2  == 0:
        return "Even"
    else:
        return "Odd"
    

number = int(input("Enter a number: "))
print(check_even_odd(number))