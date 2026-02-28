net_amount = 0

while True:
    s = input("Please enter W for withdrawal or D for deposit followed by a space and then the amount. E.g. W 800")
    if not s:
        break
    values = s.split(' ')
    if values[0].lower() == 'w':
        net_amount-=int(values[1])
    elif values[0].lower() == 'd':
        net_amount+=int(values[1])
    else:
        pass

print(net_amount)