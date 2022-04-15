import unittest
from primezz import fact, is_prime, primes


def reference_primes(x, y):
    """Boring noob solution from:
    https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval
    """
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


class PrimeExamples(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(5), 5*4*3*2*1)

    def test_prime_0(self):
        self.assertFalse(is_prime(0))

    def test_prime_1(self):
        self.assertFalse(is_prime(1))

    def test_prime_2(self):
        self.assertTrue(is_prime(2))

    def test_prime_minus_2(self):
        # Some people may disagree here, but -2 is an ideal prime (pun intended).
        self.assertTrue(is_prime(-2))

    def test_primality_example(self):
        # Test the example from documentation.
        self.assertEqual(list(primes(11, 42)), [11, 13, 17, 19, 23, 29, 31, 37, 41])


class ReferencePrime(unittest.TestCase):
    def test_primes_500(self):
        self.assertEqual(list(primes(0, 500)), reference_primes(0, 500))


if __name__ == '__main__':
    unittest.main()
