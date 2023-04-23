import sys

def stromek(times):

    CONST = 4

    s1 = ''
    buffer = [ ]
    base = '*'
    slice_ = 0
    for t in range(times):

        if len(buffer) > 1:
            if (t+1) % 2 == 0:
                slice_ += 2
            base = buffer[-1][:-slice_] # posledný riadok, mínus dve hviezdičky

        for i in range(CONST+t):
            if i == 0:
                s1 = base
            else:
                s1 += '**'
            buffer.append(s1)

    # kmen
    width = len(buffer[-1])
    for i in range(times):
        if times % 2 == 0:
            s2 = '|' *(times+1)
            s2 = s2.center(width)            
        else:
            s2 = '|' *times
            s2 = s2.center(width)

        buffer.append(s2) # kmeň do buffra    

    # samotné vykreslenie
    # width = len(buffer[-1])
    for i in buffer:
        print(i.center(width))    


arguments = sys.argv
# print(arguments)
if len(arguments) == 1:
    print(f'please provide integer number as paramater')
else:
    if int(arguments[1]) == 0:
        ...
    else:
        stromek(int(arguments[1]))

