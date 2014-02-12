'''
Problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from utils import primes

p = primes()
for i in range(10000):
    p.next()

print p.next()
