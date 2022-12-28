def filtered(itera, func):
    return list(filter( func , itera))

if __name__ == '__main__':

    mylist = [ i for i in range(101) ]

    prve1 = filtered(mylist,lambda x:x%3==0)
    print(*prve1, sep=', ')
    prve2 = filtered(mylist,lambda x:x%5==0)
    print(*prve2, sep=', ')
    prve3 = filtered(mylist,lambda x:x%15==0)
    print(*prve3, sep=', ')