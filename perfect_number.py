def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if (num % i == 0):
            sum = sum + i
    
    if num == sum:
        print(num ," is a Perfect Number")
    else:
        print(num ," is not a Perfect Number")


num = int(input("Enter a number :: "))
perfect_number(num)