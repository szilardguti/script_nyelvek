#!/usr/bin/env python3


def palindrom_recur(s):
    if(len(s) == 1):
        return str(True)
    else:
        if(s[0] == s[-1]):
            return palindrom_recur(s[1:-1])
        else:
            return str(False)


def main():
    print(palindrom_recur(input("Adjon meg egy szót: ")))


if __name__ == "__main__":
    main()
