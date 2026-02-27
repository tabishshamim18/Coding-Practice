value = []

for i in range(1000, 3000):
    counter = 0
    for j in str(i):
        if int(j) % 2==0:
            counter+=1
    if len(str(i)) == counter:
        value.append(str(i))
print(','.join(value))