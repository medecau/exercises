'''
Problem 67


By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''

t=open('067.txt').read()

t=t.split('\n')[1:]
t=[i.split(' ') for i in t]
t=[[int(j) for j in i] for i in t] # ;) thanks python

for i in range(len(t))[-2::-1]:
    for j in range(len(t[i])):
        t[i][j]+=max(t[i+1][j:j+2])

print t[0][0]









