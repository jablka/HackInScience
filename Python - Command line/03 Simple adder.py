import sys

arguments = sys.argv
# print(arguments)
if len(arguments) == 1:
    print(f'usage: python3 {arguments[0]} OP1 OP2')
else:
    cisla = map(int,arguments[1:])
    print(sum(cisla))