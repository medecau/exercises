#coding: utf8
'''
The Fibonacci sequence is defined by the recurrence relation:

    F_(n) = F_(n−1) + F_(n−2), where F_(1) = 1 and F_(2) = 1.

Hence the first 12 terms will be:

    F_(1) = 1
    F_(2) = 1
    F_(3) = 2
    F_(4) = 3
    F_(5) = 5
    F_(6) = 8
    F_(7) = 13
    F_(8) = 21
    F_(9) = 34
    F_(10) = 55
    F_(11) = 89
    F_(12) = 144

The 12th term, F_(12), is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
from time import time
start=time()

a=1
b=2
c=3
result=2
while b<pow(10,999):
  sum=a+b
  a=b
  b=sum
  c+=1

result=c


print 'The answer is: '+str(result)
print 'Calculated in '+str(round(time()-start,5))+'s.'