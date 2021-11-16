#!/usr/bin/env python3
import primecheck


def main():
    for i in range(100):
        if primecheck.is_prime(i):
            print(i,end = ' ')
    print()
    

if __name__ == "__main__":
    main()
