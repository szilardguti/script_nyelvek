#!/usr/bin/env python3

# a = "Batman" ----> a[(start):(end)] --> a start benne van, az end már nincs!!
# string indexelés 0tól indul itt is --> az elején a '0' elhagyható, a végén
# a végpozíció is elhagyható

# túlindexelésnél nem dob hibát

# a szeletelés eredménye egy új objektum


def main():
    a = "Batman"
    print(a[0])
    print(a[3:6])
    print(a[:3])
    print(a[3:])
    print(a[:])
    #támogatja a negatív indexelést is
    print(a[-3:-1])
    #megadható még egy ':' -> lépésköz
    s = "python programming"
    print(s[::2])
    print(s[::-1]) #megfordítja a stringet!
    print(s[3:0:-1])


if __name__ == "__main__":
    main()
