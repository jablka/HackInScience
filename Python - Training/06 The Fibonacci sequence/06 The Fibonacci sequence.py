def fibonacci(n):
    mylist = [ ]
    for i in range(n+1):
        if i<=1: mylist.append(i)
        else:
            mylist.append(mylist[i-1]+mylist[i-2])
    mylist.pop(0)
    return mylist