#!/usr/bin/env python3


def palindrom_recur(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrom_recur(s[1:-1])
        else:
            return False


def main():
    print("A beírt szó palindrom:", palindrom_recur(input("Adjon meg egy szót: ")))


if __name__ == "__main__":
    main()
