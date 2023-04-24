def battery_charge(n):
    count = round(n/10)
    char = '❚'
    output = '['+(char*count).ljust(10)+']'
    print(output)
    print(f'{n}%')