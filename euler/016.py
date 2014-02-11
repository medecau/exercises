'''
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
'''
from time import time
from utils import sum_digits
start=time()

result = sum_digits(pow(2,1000))

print 'The answer is: '+str(result)
print 'Calculated in '+str(round(time()-start,5))+'s.'