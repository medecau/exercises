'''
Problem 14


The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def seq_len(start):
    current_num=start
    l=0
    while current_num != 1:
        if current_num % 2 == 0:
            current_num/=2
        else:
            current_num=current_num*3+1
        l+=1
    return l

max_known=0
for i in range(1,1000000,2): #makes sense to only test odd numbers
    length=seq_len(i)
    if length>max_known:
        max_known=length
        max_num=i


print max_num