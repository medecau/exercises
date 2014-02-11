'''
Problem 10


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from mathkit import next_prime

next=2
primes=[]
while next<2000000:
    primes.append(next)
    next=next_prime(next)

print sum(primes)
