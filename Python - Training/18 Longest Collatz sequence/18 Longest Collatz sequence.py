def collatz_length(n):
    step = 0
    while n != 1:

        if n % 2 == 0: # even
            n = n // 2
            step +=1
        else:
            n = n*3 +1
            step +=1

        # print(n, step)

    return step