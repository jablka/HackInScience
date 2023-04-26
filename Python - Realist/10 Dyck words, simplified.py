def is_a_dyck_word(word: str) -> bool:

    if bool(word) == False: # word = "" , should evaluate to True
        return True

    if len(set(word)) != 2: # word should have precisely two kinds of characters
        return False

    characters = tuple(set(word))
    if word.count(characters[0]) != word.count(characters[1]):
        return False # musí byť rovnaký počet obidvoch znakov / equal count of both characters     
    
    initial = word[0] # initial character
    buffer = [ ]
    for i in range(len(word) ):

        if word[i]==initial: # if encounter initial character, append it to buffer
            buffer.append(word[i])
        
        else:
            if len(buffer)>0: 
                buffer.pop() # if we have closing character, pop the buffer
            else:
                return False # if the buffer is already empty, word can't be a 'Dyck word'

    return True
    
