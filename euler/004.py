'''
Problem 4


A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

products = (str(x*y) for x in range(999, 99, -1) for y in range(999, 99, -1))
palindromic = (int(product) for product in products
               if product == product[::-1])

answer = max(palindromic)

print(answer)
