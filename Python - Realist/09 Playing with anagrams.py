import unicodedata

def is_anagram(left, right):

    def remove_accents(input_str:str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

    left = remove_accents(left)
    right = remove_accents(right)

    new_left = [ n.lower() for n in left if n.isalpha() ]
    new_right = [ n.lower() for n in right if n.isalpha() ]

    for n in new_right:
        if n in new_left:
            new_left.pop( new_left.index(n) )
        else: 
            return False
  
    return True 

assert is_anagram('funeral', 'real fun' )
assert is_anagram('crâné', 'crane' )
assert is_anagram('Madam Curie', 'Radium came' )
