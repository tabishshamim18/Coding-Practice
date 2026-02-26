num_list = [nums for nums in input().split(',')]
divisible_by_5 = []

for i in num_list:
    int_i = int(i,2)
    if int_i%5==0:
        divisible_by_5.append(str(i))

print(','.join(divisible_by_5))