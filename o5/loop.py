#!/usr/bin/env python3


def loop(n, debug=False):
    """return numbers upto the input value"""
    if debug: print("# ciklus kezdete")
    for i in range(1,n+1):
        print(i, end=' ')
    print()
    if debug: print("# ciklus vége")


def main():
    loop(10)
    print('-' * 20)
    loop(10, debug = True)


if __name__ == "__main__":
    main()
