import unittest

def fibonacci():
    a, o=0, 1
    while True:
        a, o = o, a+o
        yield o

def fib_seq(num):
    seq=[]
    f=Fibonacci()
    for i in range(num):
        seq.append(f.next())
    return seq

def is_prime(num):
    from math import ceil
    from math import sqrt
    if (num%2 == 0 and num>2) or num < 2 or type(num) is not int:
        return False
    else:
        l=int(ceil(sqrt(num)))
        for i in xrange(3, l+1, 2):
            if num%i==0:
                return False
        return True

def next_prime(num):
    if num > 2:
        if num%2==0:
            num-=1
        else:
            pass
        while True:
            num+=2
            if is_prime(num):
                return num
            else:
                continue
    elif num == 2:
        return 3
    else:
        return 2


def primes(num=0):
    while True:
        num = next_prime(num)
        yield num

def get_factors(num, short=False):
    from math import ceil
    from math import sqrt
    factors=[]
    square=sqrt(num)
    if square.is_integer():
        factors.append(int(square))
    for f in xrange(1,int(ceil(square))):
        if num%f==0:
            factors.extend([f, int(num/f)])
    if short:
        factors.sort()
        return factors[1:-1]
    else:
        return factors

def sum_digits(num):
    sum=0
    while num>0:
        sum+=num%10
        num=int(num/10)
    return sum

def is_palindromic(val):
    s=str(val)
    s2=list(s)
    s2.reverse()
    s2=''.join(s2)
    return s==s2

class TestBatch(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_prime_1(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_2(self):
        self.assertTrue(is_prime(11))

    def test_is_prime_3(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_4(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_5(self):
        self.assertFalse(is_prime(-1))

    def test_is_prime_6(self):
        self.assertFalse(is_prime(9))

    def test_next_prime_1(self):
        self.assertEqual(next_prime(-1), 2)

    def test_next_prime_2(self):
        self.assertEqual(next_prime(1), 2)

    def test_next_prime_3(self):
        self.assertEqual(next_prime(2), 3)

    def test_next_prime_4(self):
        self.assertEqual(next_prime(3), 5)

    def test_next_prime_5(self):
        self.assertEqual(next_prime(9), 11)

    def test_get_factors_1(self):
        factors=get_factors(1)
        self.assertEqual(factors, [1])

    def test_get_factors_2(self):
        factors=get_factors(2)
        self.assertEqual(factors, [1,2])

    def test_get_factors_3(self):
        factors=get_factors(3)
        self.assertEqual(factors, [1,3])

    def test_get_factors_4(self):
        factors=get_factors(8)
        factors.sort()
        self.assertEqual(factors, [1,2,4,8])

    def test_get_factors_5(self):
        factors=get_factors(25)
        factors.sort()
        self.assertEqual(factors, [1,5,25])

    def test_get_factors_6(self):
        factors=get_factors(8, True)
        factors.sort()
        self.assertEqual(factors, [2,4])

    def test_get_factors_7(self):
        factors=get_factors(25, True)
        factors.sort()
        self.assertEqual(factors, [5])

    def test_fibonacci_1(self):
        fibonacci_nums=fib_seq(10)
        self.assertEqual(fibonacci_nums, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

def do_tests():
    batch = unittest.TestLoader().loadTestsFromTestCase(TestBatch)
    unittest.TextTestRunner().run(batch)

if __name__ == "__main__":
    do_tests()