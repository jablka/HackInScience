# this is a bit hacky version

import re

def flatten(a_list):

    mystring = str(a_list)
    # print(mystring)

    najdene = re.findall('\d+', mystring)
    result = list(map(int, najdene))
    return result