#!/usr/bin/env python3


def main():
    with open("100db_50jegyu.txt", "r") as f:
        for line in f:
            print(line[:10])


if __name__ == "__main__":
    main()
