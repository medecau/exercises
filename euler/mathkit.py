import unittest

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
            else:
                continue
        return True

def next_prime(num):
    if num > 2:
        if num&1==0:
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


def do_tests():
    batch = unittest.TestLoader().loadTestsFromTestCase(TestBatch)
    unittest.TextTestRunner().run(batch)

if __name__ == "__main__":
    do_tests()