#!/usr/bin/env python3


def palindrom_iter(s):
    i = 0
    while i < len(s)//2:
        if s[i] != s[len(s) - i - 1]:
            return False
        i += 1
    return True


def main():
    print(palindrom_iter(input("Adjon meg egy szót: ")))


if __name__ == "__main__":
    main()
