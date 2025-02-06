def duplicate_char(txt):
    char_value = {}
    duplicates_list = []
    for ch in txt:
        if ch in char_value.keys():
            char_value[ch] = char_value[ch]+1
        else:
            char_value[ch] = 1

    for ch, value in char_value.items():
        if value > 1:
            duplicates_list.append(ch)
    
    return duplicates_list

txt = str(input("Enter a string :: "))
output = duplicate_char(txt)
print(output)