FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

mylist = list()
for i in FLAVORS:
    for j in FLAVORS:
        if i != j and ([j,i] not in mylist):
                mylist.append([i,j])

# print(mylist)
for i in mylist:
    print(f'{i[0]}, {i[1]}')