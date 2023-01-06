import sys

arguments = sys.argv
operators = '+-*/%^'

if len(arguments) < 4:
    print('usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number')
else:
    if arguments[1].isdecimal and arguments[3].isdecimal and (arguments[2] in operators):

        if arguments[2] == '^':
            arguments[2] = '**'

        s = arguments[1]+arguments[2]+arguments[3]
        try:
            print(eval(s))
        except:
            print('input error')

    else:
        print('input error')
