def pallindrome_string(txt):
    txt = txt.lower()
    reverse_txt = txt[::-1]
    if reverse_txt == txt:
        return True
    else:
        return False
    
txt = str(input("Enter a string :: "))
output = pallindrome_string(txt)

if output:
    print(f"{txt} is a Pallindrome String")
else:
    print(f"{txt} is not a Pallindrome String")