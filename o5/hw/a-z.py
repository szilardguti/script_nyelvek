#!/usr/bin/env python3
import sys


def main():
    alphabet = ''.join([chr(i) for i in range(97,97+26)])
    
    if "a-z" in sys.argv[0]:
        print(alphabet)
    elif "z-a" in sys.argv[0]:
        print(alphabet[::-1])   



if __name__ == "__main__":
    main()
