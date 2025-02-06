# 153 = 1*1*1 + 5*5*5 + 3*3*3
def armstrong(n):
    num = n
    n = str(n)
    length = len(n)
    n = int(n)
    digit, sum = 0, 0

    for i in range(length):
        digit = int(n%10)
        n = n/10
        sum += pow(digit, length)
    
    if sum == num:
        print(num ," is an Armstrong Number")
    else:
        print(num ," is not an Armstrong Number")


n = int(input("Enter a number :: "))
armstrong(n)