#!/usr/bin/env python3


import sys


def hello(s):
    if (s == "Batman") or (s == "Robin"):
        print("naananananannanaananananannanaananananannanaananananannanaananananannanaananananannanaanananananna")
    else:
        print("Hello " + s + "!")
        


def main():
    name = sys.argv[1]
    hello(name)


if __name__ == "__main__":
    main()
