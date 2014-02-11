'''
n! means n x (n - 1) x ... x 3 x 2 x 1

Find the sum of the digits in the number 100!
'''
from time import time
from math import factorial
from utils import sum_digits
start=time()

f=factorial(10000)
result=sum_digits(f)

print 'The answer is: '+str(result)
print 'Calculated in '+str(round(time()-start,5))+'s.'