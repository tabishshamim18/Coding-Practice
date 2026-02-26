C = 50
H = 30

D = (int(x) for x in input().split(','))
result = []

for num in D:
    Q = ((2 * C * num)/H) ** 0.5
    result.append(str(round(Q)))
print(','.join(result))