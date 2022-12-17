import string

letters = string.ascii_lowercase

for letter in letters:
    for letter2 in letters:
        print(letter+letter2)