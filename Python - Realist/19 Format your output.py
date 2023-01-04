def list_pretty_print(items):
    count = 0
    for i in items:
        count +=1
        if count == len(items):
            print(i)
        else:    
            if count % 5 == 0:
                print(i)
            else:
                print(f'{i}, ', end='')