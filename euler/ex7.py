'''
Problem 7


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from mathkit import next_prime

counter=0
num=1
while counter < 10001:
    num=next_prime(num)
    counter+=1
print num
