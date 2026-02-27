input_string = input()
d= {"Digits": 0, "Letters": 0}

for i in input_string:
    if i.isdigit():
        d['Digits']+=1
    elif i.isalpha():
        d['Letters']+=1
    
print(f"LETTERS: {d['Letters']} DIGITS {d['Digits']}")