#!/usr/bin/env python3


def string_tisztito(s):
    return ''.join(s.split())


def main():
    print(string_tisztito("206.130.99.82:\n8080"))
    print(string_tisztito("192.20.246.138:\n 6666"))
    print(string_tisztito("\t192.\n168    .    10\t\t\t.123: 1234\n\n"))


if __name__ == "__main__":
    main()
