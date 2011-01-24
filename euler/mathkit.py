def is_prime(num):
    from math import ceil
    from math import sqrt
    if (num&1 == 0 and num>2) or num < 2 or type(num) is not int:
        return False
    else:
        l=int(ceil(sqrt(num)))
        for i in xrange(3, l, 2):
            if num%i==0:
                return False
        return True