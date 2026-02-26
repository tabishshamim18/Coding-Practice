inp_string = input()

words = sorted(set(inp_string.split(' ')))
print(', '.join(words))