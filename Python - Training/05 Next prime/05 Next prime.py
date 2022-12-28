import itertools

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

pocet = 100000000
for i in itertools.count(pocet):
    # print(i)
    if is_prime(i):
        print(i)
        break