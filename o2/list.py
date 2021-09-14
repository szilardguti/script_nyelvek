#!/usr/bin/env python3

#ne használjuk a list nevet objektumnak -> hiszen van egy ilyen beépített függvény

def main():
    a = [1, 4, 3, 10]
    print("hossza:", len(a), "\ntípusa:", type(a))
    print(a[:2])
    print(a[-2:])
    print(a[:-1])
    
    a.append(2)
    a.append('py')
    print(a)
    
    b = a[:]
    
    b[0] = 200
    print(b)
    print(a==b)
    
    
    print("B-ben:", 200 in b, "\nA-ban:", 200 in a)


if __name__ == "__main__":
    main()
