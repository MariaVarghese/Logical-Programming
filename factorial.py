def factorial(n):
    product = 1
    while(n>1):
        print(n)
        product = product * n
        n -= 1
    return product

num = int(input("Enter a number :: "))
output = factorial(num)
print(f"Factorial of {num} :: {output}")