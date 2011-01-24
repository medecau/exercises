'''
Problem 5


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# this list needs not to include all numbers from 1 to 20
# if I iterate on steps of 20 starting from 20 it will always be divisible by 20
# primes need be here for obvious reasons but the lower numbers that are divisors
# to numbers already in the list need not be included
# i'ts in reverse order because the higher the number is the least probability of
# matching 
divisors=[19,18,17,16,15,14,13,12,11]
num=0
did_not_find=True
while did_not_find:
    num+=20
    did_not_find=False
    for each in divisors:
        if num%each!=0:
            did_not_find=True
            break

print num