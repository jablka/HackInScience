import string

with open("words.txt") as file:
    data = file.read()

velkost = len(data)

for letter in string.ascii_lowercase:
    freq = data.count(letter) / velkost
    print(f'{letter}:', '{:.2f}'.format(freq))
