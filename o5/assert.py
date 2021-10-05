#!/usr/bin/env python3


def main():
    n = int(input("Adjon meg egy páratlan számot: "))
    
    assert n % 2 == 1
    
    print(f"A megadott szám: {n}")


if __name__ == "__main__":
    main()
