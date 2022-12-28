def from_roman_numeral(roman_numeral):

    mylist = [ ]
    for a in roman_numeral:
        if a == 'I':
            mylist.append(1)
        if a == 'V':
            mylist.append(5)
        if a == 'X':
            mylist.append(10)
        if a == 'L':
            mylist.append(50)
        if a == 'C':
            mylist.append(100)
        if a == 'D':
            mylist.append(500)
        if a == 'M':
            mylist.append(1000)

    vysledok = 0
    for i in range(len(mylist)):
        vysledok += mylist[i]
        if i+1<len(mylist):
            if mylist[i]<mylist[i+1]:
                vysledok -= 2*mylist[i]

    return vysledok