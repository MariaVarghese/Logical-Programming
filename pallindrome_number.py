def pallindrome_number(num):
    reverse_num = int(str(num)[::-1])
    if reverse_num == num:
        return True
    else:
        return False
    
num = int(input("Enter a number :: "))
output = pallindrome_number(num)

if output:
    print(f"{num} is a Pallindrome Number")
else:
    print(f"{num} is not a Pallindrome Number")