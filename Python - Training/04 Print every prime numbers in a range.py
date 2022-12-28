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

s = ''
for i in range(10000,10050):
    if is_prime(i):
        s += str(i)+', '
        # print(f'{i}, ', end='')
print(s[:-2])