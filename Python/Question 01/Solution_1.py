num_list = []

for i in range(2000, 5001):
    if i%7==0 and i%5!=0:
        num_list.append(str(i))
    
print(', '.join(num_list))