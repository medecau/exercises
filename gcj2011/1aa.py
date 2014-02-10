# -*- coding: utf-8 -*-

import sys

def test(s):
    N, PD, PG = [int(x) for x in s.split(' ')]
    if (PD!=100 and PG==100) or (PD!=0 and PG==0):
        return 'Broken'
    else:
        for n in range(N,0,-1):
            if PD%(100/n)==0:
                return 'Possible'
        return 'Broken'
        

#fin = sys.stdin
fin=open('A-small-attempt4.in')
for case in range(int(fin.readline())):
    l=fin.readline().strip()
    print 'Case #%d: %s' % (case+1, test(l))
