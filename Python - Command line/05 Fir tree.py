import sys

def stromek(times):

    CONST = 4 # štyri riadky...základ stromku

    s1 = ''
    buffer = [ ]
    base = '*'
    slice_ = 0
    for t in range(times):

        if len(buffer) > 1: # ak je viac ako jednodielový stromček (teda ak t > 0 (druhý a každý ďalší cyklus)... aj takto by sa to dalo napísať)
            if (t+1) % 2 == 0: # každý druhý cyklus sa navyšuje slice o 2
                slice_ += 2
            base = buffer[-1][:-slice_] # base bude teraz posledný riadok, mínus príslušný počet hviezdičiek

        for i in range(CONST+t): # tu sa generuje príslušný diel stromčeku
            if i == 0:
                s1 = base
            else:
                s1 += '**'
            buffer.append(s1)

    # kmeň
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

