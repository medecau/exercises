#coding: utf8
'''
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from time import time
from utils import is_prime, next_prime
start=time()

max=1000000

i=2
max_prime=2
max_factors=1
while i<max:
  sum=i
  j=next_prime(i)
  factors=1
  while sum+j<max:
    factors+=1
    sum+=j
    if factors>max_factors and is_prime(sum):
      max_factors=factors
      max_prime=sum
    j=next_prime(j)
  i=next_prime(i)


result=str(max_prime)+'-'+str(max_factors)
print 'The answer is: '+str(result)
print 'Calculated in '+str(round(time()-start,5))+'s.'