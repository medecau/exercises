'''
Problem 13


Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
nums=open('013.txt', 'r').read()

nums=nums.split('\n')

print str(reduce(lambda x, y: int(x)+int(y), nums))[:10]