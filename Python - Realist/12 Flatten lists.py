def flatten(a_list, f_list=None):

    if f_list == None:
        f_list = [ ]

    for element in a_list:
        if isinstance(element, list):
            flatten(element, f_list=f_list)
        else:
            f_list.append(element)

    return f_list