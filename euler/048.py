#coding: utf8
'''
The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).
'''
from time import time
start=time()

r=0
for i in range(1,1001):
  r+=pow(i,i)

result=str(r)[-10:]
print 'The answer is: '+str(result)
print 'Calculated in '+str(round(time()-start,5))+'s.'