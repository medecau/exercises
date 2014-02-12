'''
Problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from itertools import count


# this list needs not to include all numbers from 1 to 20
# if I iterate on steps of 20 starting from 20 it will always be divisible by 20
# primes need be here for obvious reasons but the lower numbers that are divisors
# to numbers already in the list need not be included
# i'ts in reverse order because the higher the number is the least probability of
# matching
divisors = [19,18,17,16,15,14,13,12,11]


for answer in count(20, 20):
    found = True
    for div in divisors:
        if answer % div != 0:
            found = False
            break

    if found:
        break
    else:
        continue


print answer
