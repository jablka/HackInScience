def draw_n_squares(n):
    roof = '+---'
    mid = '|   '
    floor = '+---'

    vysledok = ''
    # print(n)

    mylist = [ ]
    for i in range(n):
        roof_ = roof * n
        mid_ = mid * n
        floor_ = floor * n
        mylist.append(roof_ + '+\n' + mid_ + '|\n')

    mylist.append(floor_ + '+\n')

    for i in mylist:
        vysledok += i

    return vysledok