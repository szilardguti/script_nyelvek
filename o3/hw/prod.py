#!/usr/bin/env python3


def product(numbers):
    prod = 1
    for e in numbers:
        prod *= e
    return prod
        

def main():
    li = [1, 2, 3, 4, 5]
    print("Lista elemeinek szorzata:", product(li))
    
    lf = [1.4, 2.123, 3.412, 4.2, 5.0001]
    print("Lista elemeinek szorzata:", product(lf))


if __name__ == "__main__":
    main()
