import textwrap
import itertools

def sidebyside(left, right, width=79):
    if width % 2 == 0: # if width is even, we drop one column
        width -=1

    width -= 1 # save one column for '|' separator
    width = width // 2

    arr1 = textwrap.wrap(left,width)
    arr2 = textwrap.wrap(right,width)
    arr_ = ['|'] * max(len(arr1),len(arr2))
   
    arr1_just = []
    for a,b in itertools.zip_longest(arr1,arr_):
        if a: 
            arr1_just.append(a.ljust(width)) # even if line is wrapped fine, it may not be long enough, so have to use .ljust()
        else:
            a = ''                           # here we're filling out blank lines
            arr1_just.append(a.ljust(width))
  
    # final output
    buffer = [ ]
    for i in itertools.zip_longest(arr1_just,arr_,arr2):
        sub_buffer = [ ]
        for j in i:
            if j == None:
                j = ''
            sub_buffer.append(j)
        # a,b,c  = i
        s = "".join(sub_buffer)
        buffer.append(s)

    result = "\n".join(buffer)
    return result