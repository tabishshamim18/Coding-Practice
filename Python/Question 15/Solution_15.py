nums = input().split(',')
squares = [str(int(i)**2) for i in nums if int(i) % 2 != 0]

print(','.join(squares))