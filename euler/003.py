'''
Problem 3


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from utils import is_prime
from math import sqrt

target=600851475143
target_sqrt=int(sqrt(target))
primes = []

for e in range(3,target_sqrt,2):
    if is_prime(e):
        primes.append(e)

primes.reverse() # reversing because i'm only looking for the largest
primes.append(2) # the 2 needs to be here just in case

for e in primes:
    if target%e==0:
        print e
        break
