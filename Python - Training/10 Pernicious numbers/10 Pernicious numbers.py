def is_prime(n):
    square_root = n**0.5
    for i in range(2,int(square_root)+1):
        if n % i == 0:
            result = False
            break
    else:
        result = True
    
    if n == 1: result = False            
    return result

rozsah = range(222281, 222381)

for n in rozsah:
    if is_prime(str(bin(n)).count('1')):
        print(n)
