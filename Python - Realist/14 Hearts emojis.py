import unicodedata
for i in range(1,230000):
    name = unicodedata.name(chr(i), 'pass')
    if 'HEART' in name:
        print(chr(i), end='')
        