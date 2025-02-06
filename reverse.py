# Reverse a string
def reverse_string(txt):
    return txt[::-1]

#Reverse Number
def reverse_number(num):
    num = (str(num))[::-1]
    return int(num)

txt = str(input("Enter a string :: "))
output = reverse_string(txt)
print(output)

num = int(input("Enter a number :: "))
output = reverse_number(num)
print(output)