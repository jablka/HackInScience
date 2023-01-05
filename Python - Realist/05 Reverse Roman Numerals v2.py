def from_roman_numeral(roman_numeral):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    mylist = [ ]
    for a in roman_numeral:
        mylist.append(roman[a])

    vysledok = 0
    for i in range(len(mylist)):
        vysledok += mylist[i]
        if i+1<len(mylist):
            if mylist[i]<mylist[i+1]:
                vysledok -= 2*mylist[i]

    return vysledok