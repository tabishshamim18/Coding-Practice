def fact(num):
    result=1

    if num ==0:
        return 1
    
    for i in range(1,num+1):
        result *= i
    
    return result

x = int(input())
print(fact(x))