'''
Problem 1


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def fact(num):
    n=1
    for i in range(num, 0, -1):
        n*=i
    return n

def check(num):
    s=str(num)
    r=0
    for i in s:
        r+=fact(int(i))
    return r==num



l=[]
n=10
try:
    while True:
        if n%100==0:
            print n
        if check(n):
            print n
            l.append(n)
        n+=1
finally:
    print sum(l)


print check(145)