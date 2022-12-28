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

def sum_primes(n):
    vysledok = 0
    for i in range(1,n):
        if is_prime(i):
            vysledok += i
    return vysledok