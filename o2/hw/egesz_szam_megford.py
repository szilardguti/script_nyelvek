#!/usr/bin/env python3


def int_fordit(i):
    valasz = str(i)[::-1]
    return int(valasz)


def main():
    var = int(input("Adjon meg egy pozitív egész számot: "))
    valasz = int_fordit(var)
    print("A szám megfordítva: " + str(valasz))


if __name__ == "__main__":
    main()
