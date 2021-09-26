#!/usr/bin/env python3


def product(numbers):
    prod = 1
    for e in numbers:
        prod *= e
    return prod
        

def main():
    li = [1, 2, 3, 4, 5]
    print("Lista elemeinek szorzata:", product(li))


if __name__ == "__main__":
    main()
