#!/usr/bin/env python3


def main():
    li = [1,2,3,4,5,6,7,8,9,10]
    res = []
    
    for szam in li:
        if (szam%2==0):
            res.append(szam)
            
    for e in res:
        print(e)


if __name__ == "__main__":
    main()
