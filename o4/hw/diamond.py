#!/usr/bin/env python3


def diamond(i):
    if i % 2 == 0 or i < 0:
        print("A megadott szám érvénytelen!")
        return False
    else:
        rows = [ '*' * n for n in list(range(1, i+1, 2))+list(range(i-2, 0, -2)) ]
        for e in rows:
            print(e.center(i, ' '))
        return True


def main():
    while(not diamond(int(input("Kérem adjon meg egy páratlan számot!: ")))):
        print("Kérem próbálja még egyszer!\n")
        


if __name__ == "__main__":
    main()
