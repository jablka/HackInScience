import string

def caesar_cypher_encrypt(s, key):
    alfabet = list(string.ascii_lowercase)
    alfabet_size = len(alfabet)
    vysl = ''
    for letter in s:
        if letter.isalpha():
            index = alfabet.index(letter.lower()) + key
            index = index % alfabet_size
            if letter.isupper():
                vysl += alfabet[index].upper()
            else:
                vysl += alfabet[index]
        else:
            vysl += letter
    # print(vysl)
    return(vysl)


def caesar_cypher_decrypt(s, key):
    alfabet = list(string.ascii_lowercase)
    alfabet_size = len(alfabet)
    vysl = ''
    for letter in s:
        if letter.isalpha():
            index = alfabet.index(letter.lower()) - key
            index = index % alfabet_size
            if letter.isupper():
                vysl += alfabet[index].upper()
            else:
                vysl += alfabet[index]
        else:
            vysl += letter
    # print(vysl)
    return(vysl)
