#!/usr/bin/env python3


def int_fordit(i):
    valasz = i[::-1]
    return int(valasz)


def main():
    i = input("Adjon meg egy pozitív egész számot: ")
    valasz = int_fordit(i)
    print("A szám megfordítva: " + str(valasz))


if __name__ == "__main__":
    main()
