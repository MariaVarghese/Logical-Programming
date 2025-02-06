def fibonacci(n):

    num_1, num_2 = 0, 1
    counter = 0

    if n < 0:
        print("Enter a valid Number")
    elif n == 1:
        print(num_1)
    while(counter <= n):
        print(num_1)
        sum = num_1 + num_2
        num_1, num_2 = num_2, sum
        counter = counter + 1

n = int(input("How many terms? :: "))
fibonacci(n)