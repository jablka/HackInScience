def sort_by_mark(my_class):
    return sorted(my_class, key = lambda a : a[0], reverse = True)


def sort_by_name(my_class):
    return sorted(my_class, key = lambda a : a[1])


my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

print(sort_by_mark(my_class))
print(sort_by_name(my_class))
