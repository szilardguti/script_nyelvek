#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# További sztring műveletek


# E. verbing
def verbing(s):
    if(len(s) >= 3):
        if(s[-3:] == "ing"):
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


# F. not_bad
def not_bad(s):
    ni = s.find("not")
    bi = s.find("bad", ni)
    
    if(ni != -1 and bi > ni):
        s = s[:ni] + "good" + s[bi+3:]
        return s
    else:
        return s
   

# G. front_back
def front_back(a, b):
    
    if(len(a) % 2 == 0):
        ak = int((len(a)/2))
        ae = a[:ak]
        av = a[ak:]
    else:
        ak = int((len(a)/2)+1)
        ae = a[:ak]
        av = a[ak:]
        
    if(len(b) % 2 == 0):
        bk = int((len(b)/2))
        be = b[:bk]
        bv = b[bk:]
    else:
        bk = int((len(b)/2)+1)
        be = b[:bk]
        bv = b[bk:]

    return ae + be + av + bv


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

if __name__ == '__main__':
    main()
