#!/usr/bin/env python3


def palindrom2(s):
    return (s == s[::-1])


def main():
    while(1):
        print(palindrom2(input()))


if __name__ == "__main__":
    main()
