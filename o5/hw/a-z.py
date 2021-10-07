#!/usr/bin/env python3
import sys


def main():
    alphabet = ''.join([chr(i) for i in range(97,97+26)])
    
    if sys.argv[0][2:2+3] == "a-z":
        print(alphabet)
    elif sys.argv[0][2:2+3] == "z-a":
        print(alphabet[::-1])   



if __name__ == "__main__":
    main()
