import math

def prime_number(num):
    if num == 0 or num == 1:
        return  False
    elif num == 2:
        return  True
    
    prime = False

    for n in range(2, num):
        if num%n == 0:
            prime = False
        else:
            prime = True

    return prime
        
num = int(input("Enter a number :: "))
output = prime_number(num)
print(output)
if output:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")