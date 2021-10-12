#!/usr/bin/env python3


def median_calc(li):
    li = sorted(li)
    if len(li) % 2 != 0:
        return li[len(li)//2]
    else:
        return (li[len(li)//2]+li[len(li)//2-1])/2

def main():
    li = [0, 5, -2, 1, 42]
    print(median_calc(li))
    
    li.append(3)
    print(median_calc(li))

    
if __name__ == "__main__":
    main()
