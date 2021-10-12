#!/usr/bin/env python3
    
    
def szamjegy_calc(i):
    return sum([ int(v) for v in [ c for c in str(abs(i))] ])


def main():
    print(szamjegy_calc(2**1000))


if __name__ == "__main__":
    main()
