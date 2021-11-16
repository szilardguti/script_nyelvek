#!/usr/bin/env python3
from primecheck import is_prime


def main():
    primes = [i for i in range(200) if is_prime(i)]

    print(sum(primes))


if __name__ == "__main__":
    main()
