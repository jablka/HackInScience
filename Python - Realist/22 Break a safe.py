import itertools
mylist = [1,5,8]
product = list(itertools.product(mylist, repeat=4))
for i in product:
    if (1 in i) and (5 in i) and (8 in i):
        print(*i, sep=' ')