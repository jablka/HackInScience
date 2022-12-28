rozsah = range(1500, 1700)
rozsah = range(0, 1000)

for n in rozsah:
    if n % 7 == 0:
        nstring = str(n)
        mylist = [ int(cislica) for cislica in nstring ]
        # print(mylist)
        if sum(mylist) % 3 == 0:
            print(n)
