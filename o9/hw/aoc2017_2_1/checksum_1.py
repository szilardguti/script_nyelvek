#!/usr/bin/env python3

def checksum(li):
    max = li[0]
    min = li[0]
    for i in li:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max - min


def main():
    with open("input.txt", "r") as olvas:
    #az input.txt-ben a feladat weboldalán található táblázat van lementve
        sum = 0
        for row in olvas:
            li = [int(s) for s in row.split()]
            sum += checksum(li)
        print(sum)


if __name__ == "__main__":
    main()
