# -*- coding: utf-8 -*-

import sys
from itertools import combinations


def solve(ncandy, candy):
    candy=candy.strip().split(' ')
    combos=[]
    candy=[int(x) for x in candy]
    for i in range(1,len(candy)):
        for combo in combinations(candy,i):
            patrick=reduce(lambda x, y: x|y, combo)
            sean = reduce(lambda x, y: x|y, [x for x in set(candy)-set(combo)])
            sean_value=sum([x for x in set(candy)-set(combo)])
            if patrick>sean :
                print str(patrick)+'>'+str(sean)+'//'+str(combo)+' > '+str(set(candy)-set(combo)) + '//'+str(sean_value)
            else:
                #print 'NO   '+str(patrick)+'>'+str(sean) + '  '+str(set(candy)-set(combo))
                pass
    return candy

#fin = sys.stdin
fin=open('Clocal.txt')
for case in range(int(fin.readline())):
    print 'Case #%d: %r' % (case+1, solve(int(fin.readline()), fin.readline()))
    