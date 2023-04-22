from itertools import tee

def print_pascal_triangle(height):
    
    def pairwise(iterable): # Python 3.10 has it in Standard Library
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def final_print(arr):
        """ function for final print """

        # first find the width of the final row
        s = ''
        for b in arr[-1]:
            s += str(b)+'   '
        width = len(s[:-3])
        # print(width)                        

        # now print the tree / triangle
        for i in arr:
            # print(*i)        
            s = ''
            for b in i:
                s += str(b)+'   '
            s = s[:-3]
            print(s.center(width))         

        # print(arr)


    if height == 0:
        arr = [[]]
    elif height == 1:
        arr = [[1]]
    elif height == 2:
        arr = [[1],[1,1]]
    else:
        arr = [[1],[1,1]]
        for i in range(2,height): # if height >= 3
            row = []
            for b in pairwise(arr[i-1]):
                row.append(sum(b))

            row.insert(0,1)
            row.append(1)

            arr.append(row)
            
    # print(type(arr))
    final_print(arr) 
        