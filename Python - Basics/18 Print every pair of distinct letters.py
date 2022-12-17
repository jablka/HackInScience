import string

def unique_pairs():
    letters = string.ascii_lowercase

    for letter in letters:
        for letter2 in letters:
            if letter == letter2:
                continue
            print(letter+letter2)

unique_pairs()