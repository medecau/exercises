'''
Problem 36


The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_palindromic(s):
    return s==s[::-1]


print is_palindromic('roflol')
print bin(585)[2:]

l=[]
for i in range(1000000):
    if i%100000==0:
        print bin(i)
    if is_palindromic(str(i)) and is_palindromic(str(bin(i))[2:]):
        l.append(i)

print sum(l)
        


