#!/usr/bin/env python3


def negy_ossz_ossz_negy(i):
    negyzetosszeg = sum([ i**2 for i in range(1, i+1) ])
    osszeg_negyzet = sum( range(1, i+1) )**2
    return osszeg_negyzet - negyzetosszeg


def main():
    print("Az első száz természetes szám összegének a négyzete és az első száz természetes szám négyzetösszege közti különbség:", negy_ossz_ossz_negy(100))


if __name__ == "__main__":
    main()
