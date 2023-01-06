def to_roman_numeral(number):
    
    zostatok = number
    result = [ ]
     
    letters = ['M','C','X','I']
    enumer =  [1000,100,10,1]
    letters_5 =['M', 'D','L','V']
    #         [  0, 500, 50, 5]
    z = 0

    while z < len(enumer): 

        delene, zostatok = divmod(zostatok, enumer[z])    

        if delene <= 3:  
            result.append(delene*letters[z])

        elif delene == 4:
            result.append(letters[z] + letters_5[z])    

        elif 5 <= delene <= 8:
            result.append(letters_5[z] + (delene % 5)*letters[z])     

        elif delene == 9:
            result.append(letters[z] + letters[z-1])
        
        z +=1

    # print(result)
    return ''.join(result)