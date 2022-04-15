from typing import Iterator
from sys import argv


def fact(i: int) -> int:
    return 1 if i <= 1 else i * fact(i - 1)


def is_prime(i: int) -> bool:
    """Check primality using Wilson. """
    return (fact(i - 1) + 1) % i == 0


def primes(s: int, e: int) -> Iterator[int]:
    """List primes in interval. """
    return filter(lambda x: is_prime(abs(x)), range(s, e))


def main():
    if len(argv) - 1 != 2:
        print(f"Usage: {argv[0]} START END")
        print(f"\nExample {argv[0]} 11 42")
        exit(1)

    print(list(primes(int(argv[1]), int(argv[2]))))

