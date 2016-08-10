'''
Problem 15


Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
import itertools
import sys


side = int(sys.argv[1])

rows = [[1] * (side+1)]
for i in range(side):
    current_row = list([1])
    for j in range(1, side+1):
        current_row.append(current_row[-1]+rows[-1][j])
    rows.append(current_row)
for r in rows:
    print('\t'.join(str(i) for i in r))

print(rows[-1][-1])
