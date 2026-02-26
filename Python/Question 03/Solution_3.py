def squares(num):
    return {i:i**2 for i in range(1,num+1)}

x = int(input())
print(squares(x))