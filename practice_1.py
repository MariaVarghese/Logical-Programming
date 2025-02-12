def print_div(n):
    if n % 3 == 0 and n % 5 == 0:
        print("hello world")
    elif n % 3 == 0:
        print("hello")
    elif n % 5 == 0:
        print("world")

def len_comb(n):
    num = str(n)
    length = len(num)
    combination = []

    for i in range(length):
        for j in range(i+1, length):
            if (int(num[i]) + int(num[j]) == length):
                combination.append((num[i], num[j]))
    
    print(combination)

def print_pattern():
    T1 = ["C1", "a", "b", "c"]
    T2 = ["C2", "2", "1", "3"]

    combined_list = [f"{T1[0]}|{T2[0]}"]
    for i in range(1, len(T1)):
        combined_list.append(f"{T1[i]}|{T2[i]}")

    for row in combined_list:
        print(row)

def count_vow_const(text):
    vowels = 'aeiouAEIOU'
    vowels_count = 0
    consonants_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print(f"Given String Input :: {text} and Number of Vowels :: {vowels_count} and Consonants :: {consonants_count}")

# num = int(input("Enter a number : "))
# print_div(num)
# len_comb(num)
# print_pattern()
text = str(input("Enter a text :: "))
count_vow_const(text)