#!/usr/bin/env python3


def main():
    with open("teszt", "r") as f:
        for lines in f:
            lines = lines.rstrip('\n')
            print(lines)

if __name__ == "__main__":
    main()
