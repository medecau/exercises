'''
Problem 30


Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''


def precheck(num):
    return int(str(num)[0])**5

def sumpowerdigits(num):
    num=str(num)
    r=0
    for i in num:
        r+=int(i)**5
    return r
try:
    n=10
    nums=[]
    while True:
        if n%10000==0:
            print "-%d" % n
        if sumpowerdigits(n)==n:
            nums.append(n)
            print n
        n+=1
finally:
    print sum(nums)