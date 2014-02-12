'''
Problem 3


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from utils import is_prime
from math import sqrt
import sys


try:
    num = int(sys.argv[1])
except:
    num = 600851475143

target_sqrt = int(sqrt(num))
primes = []


answer = max(n for n in range(3, target_sqrt, 2)
             if num % n == 0 and is_prime(n))

print (answer)
