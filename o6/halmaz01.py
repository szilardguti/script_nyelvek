#!/usr/bin/env python3


def no_duplicate(li):
    return sorted(set(li))
    

def main():
    li = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    
    print(no_duplicate(li))


if __name__ == "__main__":
    main()
